class Cell:
    """
    Cell class represents the smallest unit of the minesweeper board.

    Attributes:
    - isMine (bool): Indicates whether the cell contains a mine.
    - isClicked (bool): Indicates whether the cell has been clicked by the user.
    - isFlagged (bool): Indicates whether the cell has been flagged by the user.
    - numNeighbors (int): Number of neighboring cells containing mines.

    Author: Ayush
    """

    def __init__(self):
        """
        Initializes a Cell instance with default attributes.

        Attributes:
        - isMine (bool): Defaults to False.
        - isClicked (bool): Defaults to False.
        - isFlagged (bool): Defaults to False.
        - numNeighbors (int): Defaults to -1.
        """
        self.__isMine = False
        self.__isClicked = False
        self.__isFlagged = False
        self.__numNeighbors = -1

    def is_mine(self) -> bool:
        """
        Returns whether the cell contains a mine.

        Returns:
        - bool: True if the cell contains a mine, False otherwise.
        """
        return self.__isMine

    def set_mine(self, is_mine: bool):
        """
        Sets the cell as containing a mine or not.

        Parameters:
        - is_mine (bool): True if the cell contains a mine, False otherwise.
        """
        self.__isMine = is_mine

    def is_clicked(self) -> bool:
        """
        Returns whether the cell has been clicked by the user.

        Returns:
        - bool: True if the cell has been clicked, False otherwise.
        """
        return self.__isClicked

    def set_clicked(self, is_clicked: bool):
        """
        Sets the cell as clicked or not.

        Parameters:
        - is_clicked (bool): True if the cell has been clicked, False otherwise.
        """
        self.__isClicked = is_clicked

    def is_flagged(self) -> bool:
        """
        Returns whether the cell has been flagged by the user.

        Returns:
        - bool: True if the cell has been flagged, False otherwise.
        """
        return self.__isFlagged

    def set_flagged(self, is_flagged: bool):
        """
        Sets the cell as flagged or not.

        Parameters:
        - is_flagged (bool): True if the cell has been flagged, False otherwise.
        """
        self.__isFlagged = is_flagged

    def get_num_neighbors(self) -> int:
        """
        Returns the number of neighboring cells containing mines.

        Returns:
        - int: Number of neighboring cells containing mines.
        """
        return self.__numNeighbors

    def set_num_neighbors(self, num_neighbors: int):
        """
        Sets the number of neighboring cells containing mines.

        Parameters:
        - num_neighbors (int): Number of neighboring cells containing mines.
        """
        self.__numNeighbors = num_neighbors

    def __str__(self) -> str:
        """
        Returns a string representation of the cell.

        Returns:
        - str: String representation of the cell, which is the number of neighbor mines.
        """
        return str(self.__numNeighbors)