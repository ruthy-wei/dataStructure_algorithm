import textwrap

sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
#填充段落
print(textwrap.fill(sample_text, width=50))
#删除现有缩进
dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)
# print(sample_text)
