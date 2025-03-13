from wc_py.webcommander.auth.dto.token_dto import RequestTokenDTO


class CommonData:

    @staticmethod
    def get_request_token_dto():
        return RequestTokenDTO(
            webCommanderUrl="[YOUR_WEBCOMMANDER_URL]",
            grantType="client_credentials",
            authString="[YOUR_AUTH_STRING]",
            clientId="[YOUR_CLIENT_ID]",
            clientSecret="[YOUR_CLIENT_SECRET]",
            redirectUri="[YOUR_REDIRECT_URI]"
        )

