"""
Processing Transactions with Decorators
Context: Create a decorator that ensures that an investment function logs start and end, and handles financial errors.
"""

import functools
import logging

# Basic logging configuration
logging.basicConfig(level=logging.INFO)

def transaction_logger(func):
    """Decorator to audit critical functions."""
    # The @functools.wraps(func) decorator is essential when defining a decorator in Python.
    # Its primary purpose is to ensure that the wrapper function 'wrapper' retains important metadata from the original function 'func'.
    # This includes attributes such as:
    #   - __name__: the name of the original function,
    #   - __doc__: the documentation string (docstring),
    #   - __module__: the module in which the function was defined,
    #   - __annotations__ and others.
    # Without @functools.wraps(func), the wrapper would appear to outside tools (and even to you)
    # as simply 'wrapper', losing information about the original function it replaces.
    # This metadata preservation is vital for:
    #   - Debugging,
    #   - Introspection (using help(), inspect module, etc.),
    #   - Static analysis tools and IDE features (auto-completion, signature inspection, etc.),
    #   - Complex decorator stacking (multiple decorators) to prevent confusion.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_id = kwargs.get('user_id', 'Unknown')
        logging.info(f"Starting transaction for user: {user_id}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Transaction successful for: {user_id}\n")
            return result
        except Exception as e:
            logging.error(f"[ERROR] Critical failure in transaction for {user_id}: {str(e)}\n")
            # You could trigger an alert to GCP Monitoring or Sentry here
            raise e
    return wrapper

@transaction_logger
def buy_stock(user_id: str, ticker: str, amount: float):
    if amount <= 0:
        raise ValueError("The amount must be positive")
    print(f"\nBuying {amount} of {ticker} for {user_id}...\n")
    return True

# Execution
buy_stock(user_id="user_01", ticker="ECOPETROL", amount=500.0)
buy_stock(user_id="user_02", ticker="ECOPETROL", amount=-100.0)
