import random
#Crossword Puzzle Problem
'''
OPTIMIZATION Problem similar to Knapsack (Greedy Algorithm)
Pseudocode:

Store English words in List


grid = []*N for i in range(M) Empty Grid to be filled


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
    def rec_insert(k, numwords, agrid, used):
        the_grid = agrid Get back to original grid with only one word
        usedwords = used
        if k < 0: return 1 (OUT OF RANGE) because of the random word fleshed in grid
        count = rec_insert(k-1, count, the_grid) Get to smallest word in terms of length
        if words[k] in used: return count Continue with recursion moving upward
        Try to shoehorn word in any possible way in grid HORIZONTALLY & VERTICALLY, memoize only the LARGEST count value
        
        
        HORIZONTALLY:
        for row in range(len(the_grid)): ([0, M])
            for column in range(len(the_grid[row])): ([0, N]) ==> N X M maximum
                if the_grid[row][col] == None for col in range(column, column + len(words[k] - 1):
                    then word fits in column irrespective of common letters because No LETTERS at all in that space
                    the_grid[row][col] = words[k][col] for col in range(len(words[k]))
                    the_grid[row][col + 1] = '*'
                    count = 1 + rec_insert(k-1, count, the_grid)
                    usedwords.add(words[k])
                    solutions_queue[the_grid] = count
                    return count, the_grid
                    
            
                    
                Otherwise, we go vertically (in other words perpendicularly)given a common letter in adjacency to position 0 of words[k]
                if words[k] not in usedwords and  letteri in words[k] for i, letteri in enumerate(the_grid[row][i])
                and words[k].index(letteri) == 0:That letter must be first letter of word
                    Populate column with word if path is clear or has another common letter in right spot
                    if j == words[k].index(the_grid[row + j][i]) for j in range (len(words[k])):
                        That implies that all letters from words[k] concur with placement of letters in grid column
                        So, Populate
                        the_grid[j][i] = letterj for j, letterj in enumerate(words[k][l])
                        Go to smaller word if possible
                        count, the_grid = 1 + rec_insert(k-1, count, the_grid)
                        usedwords.add(words[k])
                        solutions_queue[the_grid] = count
                        return count, the_grid
                        
                    else: We cannot populate grid this way so we continue (next row)
                    
            if words[k] in usedwords: break out of embodying for
              
                
        
        if words[k] not in usedwords:
        VERTICALLY:
        We basically do the same as in Horizontally except we primarily operate vertically then seek
        for a horizontal (or perpendicular) correspondance
        The only thing we need to do is nest the outer for in the inner or in other words just
        reverse them
        
        OTHERWISE, we move on to the next recursive step k-1 and skip this word
        if k >= 0 and (words[k] not in usedwords: 
            count += rec_insert(k-1, count, the_grid))
        
           
        End of recursive step: This solution is complete by this point, so we can append it in queue
        solutions_queue[the_grid] = count
        
        return count
    
    optimalsolutioncount = rec_insert(len(words), count = 1, grid)
    optimalsolution = max(solutions_queue, solutions_queue.get) ==> grid with most words = OPTIMAL SOLUTION
    print(f"Optimal Grid: {optimalsolution}\n") ==>Optimal grid
    return optimalsolutioncount
    
    
BRIEF WRITE-UP:
The filling of this English word puzzle begins with a set of k words being stored in a list.
A random integer number generator selects a word directly from the list and fleshes it in the middle row of the grid
which takes the form of a list. That grid is used to form the puzzle.
A greedy algorithm is used to store as many words as possible. Like the knapsack problem,
it seeks to form the best solution with brute force.
After the list is sorted in ascending order so that the smallest words enter the grid first to maximize the 
number of inserted words, a recursive method is called upon to delve onto k = 0: the first word from k = len(words).
Our base case is when k < 0: then we return 1 which represents the random number fleshed in the grid. As soon as we reach
the last recursive phase, we attempt to place the word in each row horizontally. If there is no vacancy and the word’s 
letters do not find a correspondence with those in the row, we move on to the next one. If we find one, then the algorithm
returns the amount of words it managed to fit thus far. If we still have not managed to fit the word, we try matching it 
with one of the letters in the row but fitting it perpendicularly. If still nothing, we restart the process with fitting
them first vertically and then perpendicularly to corresponding letters (horizontally). The count of words fitted starts
at one at each recursive step before we increment at each successful fit. These steps take a dominating time complexity
of O(N x M) at worst case since we don’t always need to search the whole grid to find a viable insertion.
That said a memo for the recursive function might have quickened the algorithm. However, it would not be convenient
with the way it operates because the algorithm initially starts by fitting only one element: the smallest. Then, it moves
up trying to fit k elements starting with the largest words[k]. A memo would conserve the result of k = 0 through k = len(words)
when the fitting might be different for each word in various recursive phases as its placement in the grid must adapt with that of
a previously placed word.
The time complexity is likely to be polynomial given that the running time varies upon N and M.
If N and M are of similar values, then it may be, more narrowly, quadratic.

    
    
'''