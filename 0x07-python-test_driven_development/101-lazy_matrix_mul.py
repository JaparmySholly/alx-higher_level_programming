#!/usr/bin/python3
'''Contains a lazy_matrix_mul function for a TDD project.
'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''Multiplies 2 matrices.
    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.
    Returns:
        list: A list of lists of the products of the two given matrices.
    '''
    a = np.array(m_a, dtype=object)
    b = np.array(m_b, dtype=object)
    return np.matmul(a, b)
