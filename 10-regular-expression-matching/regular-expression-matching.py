class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        # define map of vertices
        vertices = {
            -1: {'label': 'INITIAL_STATE'}
        }
        # define map of edges
        edges = {i : [] for i in range(-1, len(p)+1)}
        in_edges = {i : [] for i in range(-1, len(p)+1)}
        
        class Edge:
            def __init__(self, origin, destination, edge_type):
                self.origin = origin
                self.destination = destination
                self.edge_type = edge_type

            def __str__(self):
                start_node = vertices[self.origin]['label']
                end_node = vertices[self.destination]['label']
                return f'({start_node})-{self.edge_type}->({end_node})'

            def __repr__(self):
                return self.__str__()

        class LiteralEdge(Edge):
            def __init__(self, literal, origin, destination):
                super().__init__(origin, destination, 'lit-edge')
                self.literal = literal

            def f(self, char):
                return char ==  self.literal
        
        class DotEdge(Edge):
            def __init__(self, origin, destination):
                super().__init__(origin, destination, '.-edge')

            def f(self, char):
                return char != ''
        
        class StarEdge(Edge):
            def __init__(self, origin, destination):
                super().__init__(origin, destination, '*-edge')

            def f(self, char):
                # allows transitioning to destination node, if destination node's in-edges (preconditions) are satisfied
                preconditions = in_edges[self.destination]
                return reduce(lambda y, e: y and e.f(char), preconditions, True)

        prev_state = -1
        for i, literal in enumerate(list(p)):
            current_state = prev_state + 1
            match literal:
                case '.':
                    edges[prev_state] += [DotEdge(prev_state, current_state)]
                    vertices[current_state] = {'label': f'{literal}-{current_state}'}
                    prev_state = current_state
                case '*':
                    # merge with previous node
                    vertex = vertices[prev_state]
                    vertex['label'] = f'{p[i-1]}{literal}-{prev_state}'
                    vertices[prev_state] = vertex

                    # add cyclic transition
                    edges[prev_state] += [StarEdge(prev_state, prev_state)]
                case _:  # default case
                    edges[prev_state] += [LiteralEdge(literal, prev_state, current_state)]
                    vertices[current_state] = {'label': f'{literal}-{current_state}'}
                    prev_state = current_state

        # add matching state
        vertices[prev_state+1] = {'label': 'FINAL_STATE'}
        # add transition to matching state
        edges[prev_state] += [LiteralEdge('', prev_state, prev_state+1)]
    
        # add transitions for skipping star states
        prev_non_star = None
        star_in_between = False
        for i, vertex in vertices.items():
            is_star = '*' in vertex['label']

            if star_in_between:
                # add edge from all previous non-preceding vertices to current vertex
                for j in range(prev_non_star, i-1):
                    edges[j] += [StarEdge(j, i)]

            if not is_star:
                prev_non_star = i
                star_in_between = False
            else:
                star_in_between = True

        # edges is really a map of out-going edges - let's create an inverse map
        for edge_set in edges.values():
            for e in edge_set:
                if e.edge_type in ['.-edge', 'lit-edge']:  # we only care about preconditions
                    in_edges[e.destination] += [e]

        next_states = [-1]
        next_states_set = set(next_states)
        found_match = False

        stack = list(s[::-1])
        
        # search the graph / simulate the automaton in O(m*n)
        while len(stack) >= 0:
            if len(next_states) == 0:
                break  # nothing left to explore

            char = stack.pop() if len(stack) > 0 else ''

            out_edges = []
            for state in next_states:
                out_edges += edges[state]

            next_states = []
            next_states_set = set()

            for e in out_edges:
                if e.f(char):
                    if vertices[e.destination]['label'] == 'FINAL_STATE':
                        found_match = True
                        break
                    if e.destination not in next_states_set:
                        next_states += [e.destination]
                        next_states_set.add(e.destination)

            if found_match:
                break

            if char == '':
                break  # end of search string, but no match

        return found_match