import asyncio, logging
from requests import Request


class SCMAuthException(Exception):
    pass

class RetriesExhausted(Exception):
    pass


class SCMService:
    __log = logging.getLogger(__name__)

    def __init__(self, session):
        self.__session = session

    async def __exec_request(self, request):
        prepared_request = self.__session.prepare_request(request)
        prepStr = f"[{prepared_request.method} {prepared_request.url}]"

        for tryCount in range(0, self.__session.retries):
            
            SCMService.__log.debug(f"Executing: {prepStr} #{tryCount}")
            response = await asyncio.to_thread(self.__session.send, prepared_request)
            
            logStr = f"{response.status_code}: {response.reason} {prepStr}"
            SCMService.__log.debug(f"Response: {logStr} #{tryCount}")

            if not response.ok:
                if response.status_code in [401, 403]:
                    SCMService.__log.error(f"{prepStr} : Raising authorization exception, not retrying.")
                    raise SCMAuthException(logStr)
                else:
                    SCMService.__log.error(f"{logStr} : Attempt {tryCount}")
            else:
                return response

        raise RetriesExhausted(f"Retries exhausted for {prepStr}")
    
    def __form_url(self, path):
        base = self.__session.base_endpoint.rstrip("/")
        suffix = path.lstrip("/")
        return f"{base}/{suffix}"
    
    
    async def _exec(self, method, path, query=None, body=None, extra_headers=None):
        return await self.__exec_request(Request(method=method, \
                                                url = self.__form_url(path), \
                                                params=query, \
                                                data=body, \
                                                auth=self.__session.auth, \
                                                headers = extra_headers))
    
    async def get_protected_branches(self, *args, **kwargs):
        raise NotImplementedError("get_protected_branches")


    async def get_default_branch(self, *args, **kwargs):
        raise NotImplementedError("get_default_branch")



