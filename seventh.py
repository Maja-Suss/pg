from abc import ABC, abstractmethod
from typing import List, Tuple

Position = Tuple[int, int]

class Piece(ABC):
    def __init__(self, color: str, position: Position):
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self) -> List[Position]:
        pass

    @staticmethod
    def is_position_on_board(position: Position) -> bool:
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self) -> str:
        return self.__color

    @property
    def position(self) -> Position:
        return self.__position

    @position.setter
    def position(self, new_postion: Position):
        self.__position = new_postion

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self) -> List[Position]:
        row, col = self.position
        moves = []
        
        direction = 1 if self.color == 'white' else -1
        
        move_one = (row + direction, col)
        if self.is_position_on_board(move_one):
            moves.append(move_one)
            
        start_row = 2 if self.color == 'white' else 7
        if row == start_row and self.is_position_on_board((row + 2 * direction, col)):
            moves.append((row + 2 * direction, col))
            
        for d_col in [-1, 1]:
            diag_move = (row + direction, col + d_col)
            if self.is_position_on_board(diag_move):
                moves.append(diag_move) 
                
        return moves


class Knight(Piece):
    def possible_moves(self) -> List[Position]:
        row, col = self.position
        moves = [
            (row + dr, col + dc)
            for dr in [-2, -1, 1, 2]
            for dc in [-2, -1, 1, 2]
            if abs(dr) != abs(dc) and dr != 0 and dc != 0
        ]
        
        return [move for move in moves if self.is_position_on_board(move)]


class Bishop(Piece):
    def possible_moves(self) -> List[Position]:
        row, col = self.position
        moves = []
        
        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for i in range(1, 8):
                new_pos = (row + i * dr, col + i * dc)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
                    
        return moves


class Rook(Piece):
    def possible_moves(self) -> List[Position]:
        row, col = self.position
        moves = []
        
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for i in range(1, 8):
                new_pos = (row + i * dr, col + i * dc)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
                    
        return moves


class Queen(Piece):
    def possible_moves(self) -> List[Position]:
        rook_moves = Rook(self.color, self.position).possible_moves()
        bishop_moves = Bishop(self.color, self.position).possible_moves()
        return rook_moves + bishop_moves


class King(Piece):
    def possible_moves(self) -> List[Position]:
        row, col = self.position
        moves = []
        
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                    
                new_pos = (row + dr, col + dc)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                    
        return moves


if __name__ == "__main__":
    
    knight = Knight("black", (1, 2))
    print(knight)
    print(knight.possible_moves())

    white_pawn = Pawn("white", (2, 4)) 
    print(white_pawn)
    print(white_pawn.possible_moves())
    