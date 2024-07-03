# midterm
Design pattern explaniation:


For test case files: we use the Mock object pattern. The testing code that is given simulates the behavior of dependencies and tests the addCommand class independently by utilizing the Mock Object Pattern. You can successfully manage edge situations, assure accurate behavior under a variety of scenarios, and validate interactions by utilizing fake objects. This method is necessary to write unit tests that are dependable and strong.

For Calculation files: The Template Method pattern is utilized by the addCommand class, which defines an algorithm (execute) with stages that adhere to an organized procedure. This makes it possible to define particular behavior (error management and input processing) in the subclass and to perform command execution consistently. Using this pattern, you may make a set of instructions that have the same general structure but different implementations.

For main.py file: In main.py file, to allow for dynamic plugin loading and modular command registration, the architecture makes use of the Command Pattern, which offers flexibility and extensibility. Providing a strong foundation for command-based applications, the App class coordinates the startup, configuration, and execution flow.
For history.py file:  The State Pattern is shown with the historyCommand class, which adapts its actions to the user's input. By offering an organized method for handling various stages inside the command, this pattern improves readability and maintainability.
For env_command.py file: A practical use of the Command Pattern, the envCommand class encapsulates environment variable setting activities. Through dynamic behavior changes in response to user input, it also illustrates parts of the State Pattern and Strategy Pattern. When managing various settings inside the program, this combination offers a scalable and adaptable method.
