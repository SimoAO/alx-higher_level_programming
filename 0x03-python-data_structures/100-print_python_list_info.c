#include <Python.h>

/**
 * print_python_list_info - a function that prints some
 * basic info about python lists
 * @p: pointer to python object
 *
 * Return: no return
 */

void print_python_list_info(PyObject *p)
{
	size_t pysize = PyList_Size(p);
	size_t i = 0;
	PyListObject *plo = (PyListObject *)p;

	printf("[*] Size of the Python List = %lu\n", pysize);
	printf("[*] Allocated = %lu\n", plo->allocated);
	for (; i < pysize; i++)
	printf("Element %lu: %s\n", i, Py_TYPE(plo->ob_item[i])->tp_name);
}
