import cartopy.crs as ccrs
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
from cartopy.util import add_cyclic_point

CART_KW = dict(transform=ccrs.PlateCarree())


class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, vcenter=None, clip=False):
        self.vcenter = vcenter
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.vcenter, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))


def use_paper_style():
    """Load custom matplotlib style sheet."""
    plt.style.use("util_paper.mplstyle")


def draw_scalar_cube(
    cube,
    ax,
    method="contourf",
    cax=None,
    cbar_ttl=None,
    cbar_ticks=None,
    use_cyclic=True,
    **plt_kw,
):
    """
    Plot a cube on a map.
    Parameters
    ----------
    cube: iris.cube.Cube
        Cube to plot.
    ax: matplotlib.axes._subplots.AxesSubplot
        Cartopy axes.
    method: str, optional
        Method of plotting, e.g. "contour", "pcolormesh", etc.
    cax: matplotlib.axes._subplots.AxesSubplot or similar
        Axes for the colorbar.
    tex_units: str, optional
        TeX string of cube units to be attached to the colorbar.
    cbar_ticks: sequence, optional
        Colorbar ticks.
    use_cyclic: bool, optional
        Use `cartopy.utils.add_cyclic_point` for the data.
    plt_kw: dict, optional
        Keywords for the plotting method.
    Returns
    -------
    Result of the plotting method.
    """
    lons = cube.coord("longitude").points
    lats = cube.coord("latitude").points
    cb_ttl_kw = dict(fontsize="x-small", pad=5)

    if use_cyclic:
        _data, _lons = add_cyclic_point(cube.data, coord=lons)
    else:
        _data, _lons = cube.data, lons
    h = getattr(ax, method)(_lons, lats, _data, **plt_kw, **CART_KW)
    if cax is not None:
        cb = ax.figure.colorbar(h, cax=cax, orientation="horizontal", shrink=0.5)
        cb_ttl_kw = dict(fontsize="x-small", pad=5)
        if cbar_ttl is not None:
            cb.ax.set_title(f"{cbar_ttl}")  # , **cb_ttl_kw)
        if cbar_ticks is not None:
            cb.set_ticks(cbar_ticks)
    return h


def draw_vector_cubes(
    u,
    v,
    ax,
    cax=None,
    tex_units=None,
    cbar_ticks=None,
    mag=(),
    xstride=1,
    ystride=1,
    add_wind_contours=False,
    qk_ref_wspd=None,
    **plt_kw,
):
    """
    Plot vectors of two cubes on a map.
    Parameters
    ----------
    u: iris.cube.Cube
        X-component of the vector.
    v: iris.cube.Cube
        Y-component of the vector.
    ax: matplotlib.axes._subplots.AxesSubplot
        Cartopy axes.
    cax: matplotlib.axes._subplots.AxesSubplot or similar
        Axes for the colorbar.
    tex_units: str, optional
        TeX string of cube units to be attached to the colorbar.
    cbar_ticks: sequence, optional
        Colorbar ticks.
    mag: tuple, optional
        Tuple of numpy arrays to be used for colour-coding the vectors.
    xstride: int, optional
        Stride x-component data.
    ystride: int, optional
        Stride y-component data.
    add_wind_contours: bool, optional
        Add contours of the vector magnitude (wind speed).
    qk_ref_wspd: float, optional
        Reference vector magnitude (wind speed).
        If given, a reference arrow (quiver key) is added to the figure.
    plt_kw: dict, optional
        Keywords passed to quiver().
    """
    cb_ttl_kw = dict(fontsize="x-small", pad=5)
    xsl = slice(xstride, -xstride, xstride)
    ysl = slice(ystride, -ystride, ystride)

    lons = u.coord("longitude").points
    lats = u.coord("latitude").points

    h = ax.quiver(
        lons[xsl], lats[ysl], u.data[ysl, xsl], v.data[ysl, xsl], *mag, **plt_kw
    )
    if cax is not None and mag:
        cb = ax.figure.colorbar(h, cax=cax)
        if tex_units is not None:
            cb.ax.set_title(f"[{tex_units}]", **cb_ttl_kw)
        if cbar_ticks is not None:
            cb.set_ticks(cbar_ticks)

    if qk_ref_wspd is not None:
        ax.quiverkey(
            h,
            0.595,
            0.16,
            qk_ref_wspd,
            fr"${qk_ref_wspd}$" + r" $m$ $s^{-1}$",
            labelpos="N",
            labelsep=0.05,
            coordinates="figure",
            color="#444444",
            fontproperties=dict(size="small"),
        )

    if add_wind_contours:
        wspd = (u ** 2 + v ** 2) ** 0.5
        ax.contour(
            lons,
            lats,
            wspd.data,
            transform=plt_kw["transform"],
            levels=np.arange(30, 105, 5),
            cmap="Greens",
        )
