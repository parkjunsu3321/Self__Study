from abc import ABC, abstractmethod

class SocialLogin(ABC):
    @abstractmethod
    def login(self, code: str):
        pass

class NaverLogin(SocialLogin):
    def login(self, code: str):
        print(f"네이버 로그인 완료 (code: {code})")

class GoogleLogin(SocialLogin):
    def login(self, code: str):
        print(f"구글 로그인 완료 (code: {code})")

class KaKaoLogin(SocialLogin):
    def login(self, code: str):
        print(f"카카오 로그인 완료 (code: {code})")

class SocialLoginFactory:
    _providers = {
        "naver": NaverLogin,
        "google": GoogleLogin
    }

    @staticmethod
    def add_providers(name,instance):
        SocialLoginFactory._providers[name.lower()] = instance

    @staticmethod
    def create_login(provider: str) -> SocialLogin:
        provider = provider.lower()
        if provider in SocialLoginFactory._providers:
            return SocialLoginFactory._providers[provider]()
        else:
            raise ValueError(f"지원하지 않는 로그인 제공자: {provider}")

if __name__ == "__main__":
    SocialLoginFactory.add_providers("kakao", KaKaoLogin)
    providers = ["naver", "google", "kakao"]
    codes = ["1234", "5678", "91011"]
    for provider, code in zip(providers, codes):
        social_login = SocialLoginFactory.create_login(provider)
        social_login.login(code)