import logging
from typing import List
from os.path import join

from azure.servicebus import ServiceBusClient
from azure.servicebus import Message
from azure.servicebus import ReceiveSettleMode


def get_all_dead_letter_ids(queue_name: str,
                            client: ServiceBusClient) -> List[str]:
    """Obtain deadletter id's from specified queue
    Shout out to Sam.
    Args:
        queue_name: name of queue to query
        client: ServiceBusClient object
    Returns:
        a list of deadletter id's in queue
    """
    logging.info(f"--> Getting dead letters from '{queue_name}'...")
    dead_letters = []
    queue = client.get_queue(queue_name)
    with queue.get_deadletter_receiver(idle_timeout=0.2) as dead_letter_rx:
        dead_letters += dead_letter_rx.peek(count=9999)

    dead_letter_ids = []
    for msg in dead_letters:
        dead_letter_ids.append(msg.properties.message_id.decode("utf-8"))
    logging.info(
        f"    Finished scanning. {len(dead_letters)} dead letter(s) were found."
    )
    return dead_letter_ids


def connect(connection_str: str) -> ServiceBusClient:
    """Initiate a connection to a service bus with a connection string.
    Shout out to Sam.
    Args:
        connection_str: primary connection string to connect to service bus
    Returns:
        a ServiceBusClient object
    """
    return ServiceBusClient.from_connection_string(connection_str)


