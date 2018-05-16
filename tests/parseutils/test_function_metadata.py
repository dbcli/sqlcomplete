from sqlcomplete.parseutils.meta import FunctionMetadata, ColumnMetadata


def test_function_metadata_eq():
    f1 = FunctionMetadata(
        's', 'f', ['x'], ['integer'], [], 'int', False, False, False, None
    )
    f2 = FunctionMetadata(
        's', 'f', ['x'], ['integer'], [], 'int', False, False, False, None
    )
    f3 = FunctionMetadata(
        's', 'g', ['x'], ['integer'], [], 'int', False, False, False, None
    )
    assert f1 == f2
    assert f1 != f3
    assert hash(f1) == hash(f2)
    assert hash(f1) != hash(f3)
    assert f1.has_variadic() == False
    assert repr(f1) == "FunctionMetadata(schema_name='s', func_name='f', arg_names=('x',), arg_types=('integer',), arg_modes=None, return_type='int', is_aggregate=False, is_window=False, is_set_returning=False, arg_defaults=())"
    assert f1.args() == [ColumnMetadata(name='x', datatype='integer', foreignkeys=[], default=None, has_default=False)]
    assert f1.fields() == [ColumnMetadata(name='f', datatype='int', foreignkeys=[], default=None, has_default=False)]
