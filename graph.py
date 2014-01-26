class Graph(object):
	"""
	Represents a directed graph.
	"""

	def __init__(self):
		"""
		 Initializes the Graph to an empty graph with no nodes or edges.
		"""
		self._nodes = {}

	
	def add_node(self, node):
		"""
		If node is already in the graph, returns False and does not modify the graph.
        Otherwise, adds node to the graph and returns True.
		"""
		if node in self._nodes:
			return False
		self._nodes[node] = set()
		return True


	def has_node(self, node):
		"""
		Returns True if node is a node in the graph.
		"""
		return node in self._nodes


	def add_edge(self, node1, node2):
		"""
		Requires: node1 and node2 are nodes in self.
        Modifies: self
        Adds an edge from node1 to node2 to self.
		"""
		assert self.has_node(node1)
		assert self.has_node(node2)
		self._nodes[node1].add(node2)


	def get_nodes(self):
		"""
		Returns a frozenset containing the nodes in the graph.
		"""
		return frozenset(self._nodes)


	def get_outlinks(self, node):
		"""
		Requires: node is a node in self.
        Returns a frozenset of the nodes to which node is connected.
		"""
		assert self.has_node(node)
		return frozenset(self._nodes[node])


	def get_inlinks(self, target):
		"""
		Requires: node is a node in self.
        Returns a set of the nodes that are connected by an edge to node.
		"""
		inlinks = []
		#iteritems enables looping through a dictionary by key (source), value (sink)
		for source, sink in self._nodes.iteritems():
			if target in sink:
				inlinks.append(source)
		return set(inlinks)


	def __str__(self):
		"""
		Returns a string representation of the graph.
		"""
		res = "<graph "
		res += '; '.join(map(lambda node: str(node) + " -> " + ", ".join(map(lambda target: str(target), self.get_outlinks(node))), self._nodes))
		res += ">"
		return res


###### Alternate, implementation of __str__:

#def __str__(self):
#    """
#    Returns a string representation of the graph. 
#    """
#    res = "<graph "
#    count_outer = 0;
#    for node in self.get_nodes():
#        res = res + node + " -> "
#        count_outer = count_outer + 1
#        count_inner = 0;
#        for target in self.get_outlinks(node):
#            count_inner = count_inner + 1;
#            res = res + str(target)
#            # Add a comma if it's not after the last element in the set
#            if count_inner != len(self.get_outlinks(node)):
#                res = res + ","
#        # Add a semicolon if it's not after the last element in the set
#        if count_outer != len(self.get_nodes()):
#            res = res + "; "
#    res = res + ">"
#
#    return res











