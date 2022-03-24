#include<Python.h>

static PyObject *bhash(PyObject *self,PyObject *args)
{
    int b;
    if(!PyArg_ParseTuple(args,"i",&b)) return NULL;
    int result=((b|((b<<8)&(b<<7)))|((b<<10)^(b<<8))|0x21);
    return Py_BuildValue("i", result);
}

static PyMethodDef methods[]=
{
    {"bhash",bhash,METH_VARARGS,"Hash"},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef bhm=
{
    PyModuleDef_HEAD_INIT,
    "bhash",
    "",
    -1,
    methods
};
PyMODINIT_FUNC PyInit_bhash(void)
{
    return PyModule_Create(&bhm);
}