import boolean_quotients as bq
import poset_quotient_constructor as pqc
#import numpy as np
import math
from sympy import Matrix
from sympy.polys import polytools

def bool_edge(n):
    grp = bq.Grp([tuple(range(n))])
    return pqc.Poset_quot.edgify(pqc.Poset_quot(grp))

def boolean_mat(n,i):
    poset = bool_edge(n)
    mc,mc_shifted = pqc.matrix_compositions(poset.edge_mats)
    mc.reverse()
#    print poset.vertices[n-i-1]
    mc = map(lambda x: map(int,x),mc[i])
    mc = map(list,mc)
    return mc

def single_boolean_mat(n,i):
    poset = bool_edge(n)
    mc = poset.edge_mats
#    print poset.vertices[n-i-1]
    mc = map(lambda x: map(int,x),mc[i])
    mc = map(list,mc)
    return mc

def symmetrized_evals(mat):
    return mat*(mat.T)

for n in range(4,10):
    for i in range (n/2):
        print (n,i)
        print symmetrized_evals(Matrix(boolean_mat(n,i))).eigenvals()

def comp_beta(n,i):
    k = n-2*i-1
    return float(math.pow(2,k)-1)/k

def z_b(b,poset):
    i = len(b)-1
    mat = boolean_mat(poset.rank+1,poset.rank-i)
    verts = poset.vertices[i]
    sum = np.zeros(len(verts))
    for t in xrange(len(verts)):
        if verts[t][0]== b:
            sum += mat[t]
    return sum/(comp_beta(poset.rank+1,poset.rank-i)*(poset.rank-2*(poset.rank-i)-1)+1)

def z_a(a,poset):
    i = len(a)
    mat = boolean_mat(poset.rank+1,poset.rank-i)
#    print mat
    verts = poset.vertices[i]
    sum = np.zeros(len(verts))
    print a
    for t in xrange(len(verts)):
        if a == verts[t][1]:
            sum += mat[t]
    return sum

def z_a_b(poset,a,b):
    return comp_beta(poset.rank,poset.rank - len(a))*z_b(b,poset) - z_a(a,poset)

#print polytools.factor_list(Matrix.charpoly(Matrix(boolean_mat(4,1))))


def decompose(m,k):
    m1_const = math.factorial(k)
    m2_const = int(math.pow(2,k)-1)*math.factorial(k-1)
    m1 = Matrix.zeros((m.rows,m.cols))
    m2 = Matrix.zeros((m.rows,m.cols))
    for i in xrange(m.rows):
        for j in xrange(m.cols):
            if m[i,j] == m1_const:
                   m1[i,j] = m[i,j]
            if m[i,j] == m2_const:
                   m2[i,j] = m[i,j]
    return m1,m2

#m = Matrix(boolean_mat(5,1))
#(m1,m2) = decompose(m,2)
#computes row reduced eschelon form, and then takes the rank
#print m2
#print len(m1.rref()[-1])
#print ''
#print m1
#print len(m2.rref()[-1])
#print m1
#print ''
#print m2

#print polytools.factor_list(Matrix.charpoly(m1))
#print polytools.factor_list(Matrix.charpoly(m2))
#print z_b((0,2,3,4),bool_edge(5))
#print comp_beta(5,1)
#print z_a_b(bool_edge(5),(0,2,4),(0,2,3,4))
