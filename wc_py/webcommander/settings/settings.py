from wc_py.http.wc_rest_processor import WCRestProcessor
from wc_py.webcommander.common.dto.settings_dto import SettingsListDTO
from wc_py.webcommander.settings.settings_api_url import SettingsApiUrl


class Settings(WCRestProcessor):

    def info(self) -> SettingsListDTO:
        response = self.get(url=SettingsApiUrl.SETTINGS, response_obj=SettingsListDTO())
        return response
