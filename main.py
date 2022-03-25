from collections import defaultdict

def supersort(a, k):
    counts = count_values(a, k)
    positions = get_positions(counts)
    return construct_output(a, positions)

def count_values(a, k):
  counting = [0] * (k+1)
  for i in a:
    counting[i] = counting[i] + 1
  return counting

def test_count_values():
    assert count_values([2,2,1,0,1,0,1,3], 3) == [2, 3, 2, 1]
    
def get_positions(counts):
  a = []
  b = reduce(plus,0,counts[:0])
  c = reduce(plus,0,counts[:1])
  d = reduce(plus,0,counts[:2])  
  e = reduce(plus,0,counts[:3])

  a.append(b)
  a.append(c)
  a.append(d)
  a.append(e)
  
  return a
  
def test_get_positions():
  assert get_positions([2, 3, 2, 1]) == [0, 2, 5, 7]
    
def construct_output(a, positions):
  
  list = []
  for i in a:
    list.append((positions[i]))
  return sorted(a)

def test_construct_output():
    assert construct_output([2,2,1,0,1,0,1,3], [0, 2, 5, 7]) == [0,0,1,1,1,2,2,3]
    
def count_values_mr(a, k):
    """
    Use map-reduce to implement count_values.
    This is done; you'll have to complete count_map and count_reduce.
    """
    # done.
    int2count = dict(run_map_reduce(count_map, count_reduce, a))
    return [int2count.get(i,0) for i in range(k+1)]

def test_count_values_mr():
    assert count_values_mr([2,2,1,0,1,0,1,3], 3) == [2, 3, 2, 1]
def count_map(value):

  count_map = []
  count_map.append((value,1))
  return count_map
  #print(count_map)

def count_reduce(group):

  count_reduce = []
  i = reduce(plus, 0, group[1])
  count_reduce.append(group[0])
  count_reduce.append(i)
  return tuple(count_reduce)
# the below functions are provided for use above.

def run_map_reduce(map_f, reduce_f, mylist):
    # done. 
    pairs = flatten(list(map(map_f, mylist)))
    groups = collect(pairs)
    return [reduce_f(g) for g in groups]

def collect(pairs):
    # done.     
    result = defaultdict(list)
    for pair in sorted(pairs):
        result[pair[0]].append(pair[1])
    return list(result.items())

def plus(x,y):
    # done. 
    return x + y


def scan(f, id_, a):
    # done. 
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        return f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
    
def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])
    
def flatten(sequences):
    return iterate(plus, [], sequences)