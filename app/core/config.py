from pydantic import BaseSettings


class Settings(BaseSettings):
	API_V1_STR: str = "/api/v1"
	PROJECT_NAME: str = "serverless-fastapi-lambda"
	SECRET_KEY: str
	

	class Config:
		case_sensitive = True
		env_file = ".env"

settings = Settings()