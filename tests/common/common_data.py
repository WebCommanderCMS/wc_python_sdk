from wc_py.webcommander.auth.dto.token_dto import RequestTokenDTO


class CommonData:

    @staticmethod
    def get_request_token_dto():
        return RequestTokenDTO(
            webCommanderUrl="",
            grantType="",
            authString="",
            clientId="",
            clientSecret="",
            redirectUri=""
        )

