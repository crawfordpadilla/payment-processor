from typing import Dict, List
import logging
import requests

logger = logging.getLogger(__name__)

def send_email(subject: str, body: str, recipient: str):
    """
    Sends an email to the recipient.

    Args:
        subject (str): The subject of the email
        body (str): The body of the email
        recipient (str): The recipient's email address
    """
    try:
        response = requests.post(
            "https://api.smtp.com/send-email",
            headers={'Content-Type': 'application/json'},
            json={'from': 'sender@example.com', 'to': recipient, 'subject': subject, 'body': body}
        )
        if response.status_code == 200:
            logger.info(f"Email sent to {recipient} successfully")
        else:
            logger.error(f"Failed to send email to {recipient}: {response.text}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error: {e}")

def format_currency(amount: float, currency: str) -> str:
    """
    Formats the amount as a string with the given currency.

    Args:
        amount (float): The amount to format
        currency (str): The currency to format as

    Returns:
        str: The formatted string
    """
    return f"{amount:.2f} {currency}"

def get_payment_method_types() -> List[str]:
    """
    Returns a list of available payment method types.

    Returns:
        List[str]: The list of payment method types
    """
    return ["credit_card", "paypal", "bank_transfer"]