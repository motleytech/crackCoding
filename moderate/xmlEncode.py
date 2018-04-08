'methods for parsing xml and encoding it'

ws = set([' ', '\n', '\t'])

def skipws(inp, pos, _):
    'skips whitespace - used heavily'
    while inp[pos] in ws:
        pos += 1
    return pos

def parseTagName(inp, pos, result):
    'parses a tag or attribute name which ends with either space or ='
    tag = ''
    while inp[pos] != ' ' and inp[pos] != '=':
        tag += inp[pos]
        pos += 1
    result.append(tag)
    return pos

def parseQuotedValue(inp, pos, result):
    'parses a quoted string value'
    if inp[pos] != '"':
        raise Exception('Error: Expected double quotes at %s' % inp[pos:pos+10])
    pos += 1
    value = ''
    while inp[pos] != '"':
        if inp[pos] == '\\':
            value += inp[pos]
            pos += 1
        value += inp[pos]
        pos += 1
    result.append(value)
    return pos + 1

def parseUnquotedValue(inp, pos, result):
    'parses an unquoted string value'
    pos = skipws(inp, pos, result)
    value = ''
    while inp[pos] != '<':
        value += inp[pos]
        pos += 1
    result.append(value.strip())
    return pos

def parseAttributes(inp, pos, result):
    'parse name=value pairs (terminated by "<")'
    pos = skipws(inp, pos, result)
    while True:
        pos = parseTagName(inp, pos, result)
        pos = skipws(inp, pos, result)
        if inp[pos] != '=':
            raise Exception('Error: Expected "=" at %s' % inp[pos: pos+10])
        pos += 1
        pos = parseQuotedValue(inp, pos, result)
        pos = skipws(inp, pos, result)
        if inp[pos] == '>':
            break
    return pos

def parseTagStart(inp, pos, result):
    'parse <tagname attributes>'
    pos = skipws(inp, pos, result)
    if inp[pos] == '<':
        pos = parseTagName(inp, pos+1, result)
        pos = skipws(inp, pos, result)
        pos = parseAttributes(inp, pos, result)
        if inp[pos] != '>':
            raise Exception('Error: Expected ">" at %s' % inp[pos: pos+10])
        return pos + 1
    else:
        raise Exception('Error: Bad tag start at %s' % inp[pos: pos+10])

def parseTagEnd(inp, pos, result):
    'parse </tagname>'
    pos = skipws(inp, pos, result)
    if inp[pos] == '<' and inp[pos+1] == '/':
        while inp[pos] != '>':
            pos += 1
        return pos + 1
    else:
        raise Exception('Error: Bad closing tag at %s' % inp[pos:pos+10])

def parseChildren(inp, pos, result):
    'parse children'
    pos = skipws(inp, pos, result)
    while not (inp[pos] == '<' and inp[pos+1] == '/'):
        if inp[pos] == '<':
            pos = parseElement(inp, pos, result)
        else:
            pos = parseUnquotedValue(inp, pos, result)
        pos = skipws(inp, pos, result)
    return pos


def parseElement(inp, pos, result):
    'parse an xml element'
    pos = parseTagStart(inp, pos, result)
    result.append('0')
    pos = parseChildren(inp, pos, result)
    pos = parseTagEnd(inp, pos, result)
    result.append('0')
    return pos

def test():
    'test for parse element'
    data = """
    <family lastName="McDowell" state="CA">
        <person firstName="Gayle">Some Message</person>
        <person firstName="Doyle">Other Message</person>
    </family>
    """

    result = []
    parseElement(data, 0, result)
    result = ' '.join(result)
    assert result == 'family lastName McDowell state CA 0 person firstName \
Gayle 0 Some Message 0 person firstName Doyle 0 Other Message 0 0'
    print 'done'

if __name__ == '__main__':
    test()
