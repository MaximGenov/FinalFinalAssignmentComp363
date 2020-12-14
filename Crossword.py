import random
#Crossword Puzzle Problem
'''
OPTIMIZATION Problem similar to Knapsack (Greedy Algorithm)
Pseudocode:

Store English words in List


grid = []*N for i in range(M) Empty Grid to be filled

@memo
def Crossword_Puzzle(word_set, grid, N, M, count):
    
    SORT it according to length of words in ascending order==>Smallest words will be dropped first
    word_set = {Algorithm, greed, sort, dynamique,...}
    words = [wi] for i, wi in enumerate(word_set) Put words in data structure
    words.sort(key = len)
    
    
    This function returns the number of words inserted in grid while conserving the grid solutions
    used = []
    Since we can place words vertically and horizontally two capacities N & M unlike Knapsack
    Base case:
    rand = randint(0, len(words) - 1) First word placed in middle row
    For simplicity we assume M (and N) is large enough to contain the largest word in the list
    
    grid_index = M//2 Middle row index
    Populate grid with random word in middle row
    grid[grid_index][j] = words[i][j] for j in range(len(words[i])
    grid[grid_index][j+1] = '*' Blocked square at end of word
    used.add(words[i]) Only necessary for flushed random words
    count = 1
    solution_queue = {} dictionary to conserve various solutions of crossword
    k = len(words)-1
    def rec_insert(k, numwords, agrid):
        the_grid = agrid Get back to original grid with only one word
        if k < 0: return 0 (OUT OF RANGE)
        count = rec_insert(k-1, count) Get to smallest word in terms of length
        if words[k] in used: return count Continue with recursion moving upward
        Try to shoehorn word in any possible way in grid HORIZONTALLY & VERTICALLY, memoize only the LARGEST count value
        
        HORIZONTALLY:
        for row in range(len(the_grid)):
            for column in range(len(the_grid[row])):
                if the_grid[row][col] == None for col in range(column, column + len(words[k] - 1):
                    then word fits in column irrespective of common letters because No LETTERS at all in that space
                    the_grid[row][col] = words[k][col] for col in range(len(words[k]))
                    the_grid[row][col + 1] = '*'
                    count = 1 + rec_insert(k-1, count)
                    
                Otherwise, we go vertically (in other words perpendicularly)given a common letter
                elif letteri in words[k] for i, letteri in enumerate(the_grid[row][i])
                and words[k].index(letteri) == 0:That letter must be first letter of word
                    Populate column with word if path is clear or has another common letter in right spot
                    if j == words[k].index(the_grid[row + j][i]) for j in range (len(words[k])):
                        That implies that all letters from words[k] concur with placement of letters in grid column
                        So, Populate
                        the_grid[j][i] = letterj for j, letterj in enumerate(words[k][l])
                        Go to smaller word if possible
                        count = 1 + rec_insert(k, count, the_grid)
                
                else: We cannot populate grid this way so we continue (next row)
        
        
        VERTICALLY:
        We basically do the same as in Horizontally except we primarily operate vertically then seek
        for a horizontal (or perpendicular) correspondance
        The only thing we need to do is nest the outer for in the inner or in other words just
        reverse them
        
           
        End of recursive step: This solution is complete by this point, so we can append it in queue
        solutions_queue[the_grid] = count
        
        return count
    
    print(f"Number of words inserted: {count}\n")
    return rec_insert(len(words), count = 1, grid)
    
    
    
'''