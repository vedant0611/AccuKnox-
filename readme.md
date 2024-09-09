### Answer to the questions asked in the assignment.



# Task 1: Django Signal Execution (Sync/Async)
[Code can be found in  #task1_code.py  ]
This task demonstrates that Django signals are executed synchronously by default.
By default, Django signals are executed synchronously, meaning they block the execution of the calling thread until the signal handler has completed its task.

## Code Explanation
- I have defined a Django model `MyModel`.
- A signal handler `my_signal_handler` is connected to the `post_save` signal.
- The signal handler introduces a 5-second delay to simulate a long-running task.
- When an instance of `MyModel` is created, the signal is executed synchronously, blocking further code execution until the signal handler completes.


# Task 2: Django Signal and Threading

[Code can be found in  #task2_code.py  ]

This task proves that Django signals run in the same thread as the caller by default.
Django signals run in the same thread as the caller by default. This can be proven by printing the thread IDs of both the caller and the signal handler.

## Code Explanation
- The thread ID of the main execution thread is printed before creating an instance of `MyModel`.
- The thread ID inside the signal handler `my_signal_handler` is printed.
- Both thread IDs match, demonstrating that the signal runs in the same thread as the caller.


# Task 3: Django Signals and Transactions

[Code can be found in  #task3_code.py  ]

This task shows that Django signals are part of the same database transaction as the caller.
By default, Django signals run in the same database transaction as the caller. This means that if a signal handler raises an exception, it can cause the entire transaction to roll back

## Code Explanation
- A signal handler `my_signal_handler` is defined that raises an exception.
- We use a transaction block (`transaction.atomic`) to demonstrate that when the signal handler raises an exception, the transaction is rolled back.
- After the transaction block, no instance of `MyModel` will be created due to the rollback.


# Task 4: Custom Rectangle Class

[Code can be found in  #task4_code.py  ]

This task involves creating a custom `Rectangle` class that can be iterated over to yield its dimensions.
-An instance of the Rectangle class requires length:int and width:int to be initialized.
-We can iterate over an instance of the Rectangle class.
-When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>}  followed by the width {'width': <VALUE_OF_WIDTH>}.In this implementation, when an instance of Rectangle is iterated over, it first yields a dictionary with the length and then a dictionary with the width.

## Code Explanation
- The `Rectangle` class has two attributes: `length` and `width`.
- The `__iter__` method allows us to iterate over the instance and yield dictionaries containing the length and width.
- An example is provided where a `Rectangle` instance is created and iterated over.
