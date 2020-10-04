grammar Formula;

ID: [a-zA-Z]+;
WS: [\t\r\n ]+ -> skip;
NUMBER: ('0' .. '9') + ('.' ('0' .. '9') +)?;
operation
    : left=NUMBER operator='+' right=NUMBER
    | left=NUMBER operator='%' right=NUMBER
    | left=NUMBER operator='-' right=NUMBER
    | left=NUMBER operator='*' right=NUMBER
    | left=NUMBER operator='/' right=NUMBER
    ;
