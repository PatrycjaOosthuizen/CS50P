class Jar:
  # Initialize the jar with a specified capacity.
  # If the provided capacity is less than 0, raise a ValueError.
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Incorrect capacity")
        self._capacity = capacity # Set the maximum number of cookies the jar can hold.
        self._size = 0  # Initialize the current number of cookies in the jar to zero.

  # Return a string representation of the jar, displaying cookies as "🍪".
    def __str__(self):
        return self.size * "🍪"

   # Method to add 'n' cookies to the jar.
   # Raise a ValueError if 'n' exceeds the jar's capacity or if adding 'n' would exceed current size + n.
    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceed capacity")
        if self.size +n > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += n # Increase the size by 'n' if checks pass.

  # Method to remove 'n' cookies from the jar.
  # Raise a ValueError if there are not enough cookies to withdraw.
    def withdraw(self, n):
        if self.size < n :
            raise ValueError("There are not enough cookies to withdraw")
        self._size -= n # Decrease the size by 'n' if checks pass.

  # Property to get the maximum capacity of the jar.
    @property
    def capacity(self):
        return self._capacity

  # Property to get the current number of cookies in the jar.
    @property
    def size(self):
        return self._size

# Main function to demonstrate functionality of Jar class.
def main():
    jar = Jar() # Create an instance of Jar with default capacity (12).
    jar.deposit(5)  # Deposit 2 cookies into the jar.
    jar.withdraw(2) # Withdraw 1 cookie from the jar.
    print(jar) # Print out the current state of the jar (number of cookies).

if __name__ == "__main__":
    main() # Execute main function when script is run directly.
