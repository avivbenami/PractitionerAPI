import requests
import json
import logging
from requests.exceptions import RequestException

class PractitionerManager:
    def __init__(self, config_file="config.json"):
        self._config = self._load_config(config_file)
        self._user_agent = self._config.get("User_Agent", "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0")
        self._urls = self._config.get("URL")

        self._session = requests.session()
        self._session.headers.update({"User-Agent": self._user_agent})

    def _load_config(self, config_file):
        try:
            with open(config_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Config.json file not found.")

    def _make_api_request(self, url):
        try:
            response = self._session.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logging.error(f"API request failed: {e}")
            raise

    def get_all_professions(self):
        url = self._urls["GetAllProfessions"]
        return self._make_api_request(url)

    def get_statuses(self):
        url = self._urls["GetStatuses"]
        return self._make_api_request(url)

    def get_profession(self, professionId):
        url = self._urls["GetProfession"].format(professionId=professionId)
        return self._make_api_request(url)

    def get_practitioners(self, professionId, practitionerName = "", maxResults = 100, licenseNum = "", certificate = ""):
        url = self._urls["GetPractitioners"].format(professionId=professionId, practitionerName=practitionerName, maxResults=maxResults, licenseNum=licenseNum, certificate=certificate)
        return self._make_api_request(url)
    
    def get_licenses(self, professionId, practitionerName = "", maxResults = 100, licenseNum = "", certificate = ""):
        url = self._urls["GetLicenses"].format(professionId=professionId, practitionerName=practitionerName, maxResults=maxResults, licenseNum=licenseNum, certificate=certificate)
        return self._make_api_request(url)

    def get_professions_license(self, professionId, practitionerName = "", maxResults = 100, licenseNum = "", certificate = "", pageNumber = 1):
        url = self._urls["GetProfessionsLicense"].format(professionId=professionId, practitionerName=practitionerName, maxResults=maxResults, licenseNum=licenseNum, certificate=certificate, pageNumber=pageNumber)
        return self._make_api_request(url)
    
    def get_certificates(self, professionId, practitionerName = "", maxResults = 100, licenseNum = "", certificate = "", pageNumber = 1):
        url = self._urls["GetCertificates"].format(professionId=professionId, practitionerName=practitionerName, maxResults=maxResults, licenseNum=licenseNum, certificate=certificate, pageNumber=pageNumber)
        return self._make_api_request(url)
    
    def get_professions_license_count(self, professionId, practitionerName = "", licenseNum = "", certificate = ""):
        url = self._urls["GetProfessionsLicenseCount"].format(professionId=professionId, practitionerName=practitionerName, licenseNum=licenseNum, certificate=certificate)
        return self._make_api_request(url)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        practitioner_manager = PractitionerManager()
        professions = practitioner_manager.get_all_professions()
        if professions:
            logging.info(f"Retrieved {len(professions)} professions.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
