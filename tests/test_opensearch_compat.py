import elasticsearch
from elasticsearch import Elasticsearch


def test_elasticsearch_client_uses_opensearch_compatible_headers():
    """Guard the client version and media type required by OpenSearch 2.x."""

    assert elasticsearch.__version__ == (7, 13, 4)

    client = Elasticsearch(["http://localhost:9200"])
    connection = client.transport.get_connection()

    assert connection.headers["content-type"] == "application/json"
    assert "vnd.elasticsearch" not in connection.headers["content-type"]
