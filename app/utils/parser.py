import logging
import multiprocessing
import requests
import settings

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class ProcessPol:
    def __init__(self, num_proc):
        self.num_proc = num_proc
        self.pool = None

    def __enter__(self):
        self.pool = multiprocessing.Pool(self.num_proc)
        return self.pool

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pool.close()
        self.pool.join()


def parsers_repository(language):
    result = []
    logger.info(f"Start parsers repository {language}")
    payload = {}
    list_repos = []
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc"

    response = requests.request("GET", url, headers=headers, data=payload)
    if not response:
        return
    response = response.json()
    if not 'items' in response:
        return
    for res in response['items']:
        list_repos.append({
            "name": res['name'],
            "description": str(res['description'])[:100],
            "language": res['language'],
            "url": res['url']
        })
    logger.info(f"Finish parsers repository {language}")
    return list_repos


def start_process_pool():
    list_language = [
        "javascript",
        "python",
        "java",
        "php",
        "cpp",
        "csharp",
        "go",
        "rust",
        "c",
        "assembly"
    ]
    with ProcessPol(10) as pool:
        result = pool.map(parsers_repository, list_language)

    for pool in result:
        for data in pool:
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            values = tuple(data.values())
            query = f'INSERT INTO repositories ({columns}) VALUES ({placeholders})'
            settings.app.db.execute_query(query, values)