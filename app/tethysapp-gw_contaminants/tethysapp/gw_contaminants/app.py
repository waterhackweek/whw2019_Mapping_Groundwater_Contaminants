from tethys_sdk.base import TethysAppBase, url_map_maker


class GwContaminants(TethysAppBase):
    """
    Tethys app class for Groundwater Contamination.
    """

    name = 'Groundwater Contamination'
    index = 'gw_contaminants:home'
    icon = 'gw_contaminants/images/icon.gif'
    package = 'gw_contaminants'
    root_url = 'gw-contaminants'
    color = '#27ae60'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='gw-contaminants',
                controller='gw_contaminants.controllers.home'
            ),
        )

        return url_maps
