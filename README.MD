# PractitionerAPI

API wrapper for the functions in the site https://practitioners.health.gov.il/Practitioners/1

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following dependencies.

```bash
pip install requests
```

## Usage:
```python
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        practitioner_manager = PractitionerManager()
        professions = practitioner_manager.get_all_professions()
        if professions:
            logging.info(f"Retrieved {len(professions)} professions.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
