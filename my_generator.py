from typing import  Generator
class Generates:
    def __fibonacci_generator(self) -> Generator[int, None, None]:
        """
        A generator that yields Fibonacci numbers indefinitely.

        Yields:
            int: The next number in the Fibonacci sequence.
        """
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    @staticmethod
    def start_generating() -> None:
        """
        Continuously generates and prints Fibonacci numbers in groups of 10 until the user stops the program.

        Instructions:
            - Press "Enter" to generate the next 10 Fibonacci numbers.
            - To terminate the program, press "Ctrl+D".

        Returns:
            None: This function prints Fibonacci numbers directly to the console.
        """
        self: Generates = Generates()
        fib_gen: Generator[int, None, None] = self.__fibonacci_generator()
        n: int = 10
        line_break: str = "_" * 65
        print(line_break)
        print("Note --> if you want to stop the script, Please press \"Ctrl+D\"")
        print(line_break)
        try:
            while True:
                input(f'Tap "enter" for the next {n} Fibonacci numbers')
                print(line_break)
                for _ in range(n):
                    print(next(fib_gen))
                print(line_break)
        except EOFError:
            print("\nProgram terminated.")

if __name__ == "__main__": # main method
    Generates.start_generating()

