paragraph_1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus semper nisl vehicula porta accumsan. Phasellus fermentum metus vitae metus viverra faucibus. Aenean sodales est sed vehicula tempor. Mauris porta magna non cursus posuere. Praesent pellentesque, libero et semper aliquet, risus lectus congue turpis, in tempus nibh nibh ac magna. Sed finibus rutrum erat. Nulla facilisi.'

paragraph_2 = 'In tincidunt lectus dictum, suscipit justo volutpat, rutrum massa. Integer auctor nulla sit amet massa iaculis lobortis nec vel risus. Maecenas finibus urna quis semper fermentum. Suspendisse dignissim mattis libero rutrum dapibus. Donec elit tellus, tristique ac metus ut, laoreet mattis augue. Phasellus sapien est, elementum at imperdiet a, porta nec enim. Suspendisse potenti. Donec malesuada arcu venenatis ligula elementum aliquam. Donec vestibulum elementum nisl eget scelerisque.'

paragraph_3 = 'Vivamus id aliquam elit. Donec laoreet tincidunt lectus, porta pretium quam volutpat a. Pellentesque a velit sit amet risus ultrices consectetur. Nunc pretium pretium nisl et pretium. Ut vehicula lobortis augue id ultricies. Suspendisse pulvinar rhoncus elit, non ultricies mi. Praesent sit amet quam eget neque mollis iaculis. Curabitur a mattis magna. Cras eget lacinia elit. Nam at viverra est. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Integer iaculis sollicitudin purus, eu posuere enim ornare nec. Curabitur venenatis ultrices urna et suscipit. Ut tincidunt, ligula in aliquet sagittis, velit elit pulvinar quam, nec tincidunt ex metus posuere velit. Vivamus semper ornare justo, et vestibulum tellus efficitur eu.'

paragraph_4 = 'Nunc posuere nisl eget massa congue tempor. Sed aliquam ultricies metus ac mollis. Mauris tristique arcu et erat sagittis congue. Curabitur ut tempus eros. Proin non eros eu ante bibendum pulvinar. Aliquam ut justo malesuada, iaculis erat eu, ullamcorper orci. Vestibulum consequat consectetur ex, sit amet fermentum neque euismod id. Donec nec dolor ante. Mauris porta, ipsum a fermentum commodo, ante mauris laoreet mi, nec egestas ipsum sem eu erat. Sed vehicula tincidunt ante eu volutpat. Pellentesque posuere turpis nec nisi scelerisque, vitae luctus neque placerat. Vestibulum et nisi et neque faucibus commodo id sit amet elit. Nulla eros est, lacinia auctor ipsum quis, consequat dapibus elit.'

paragraph_5 = 'Nulla pretium ipsum ut massa varius, vitae euismod justo imperdiet. Phasellus vel turpis nunc. Phasellus vestibulum rhoncus purus. Vestibulum malesuada mi eget bibendum ultricies. Vestibulum orci quam, malesuada sit amet nunc nec, tristique tempus odio. Duis suscipit gravida faucibus. Cras non bibendum massa, quis commodo nisl. Phasellus mattis malesuada congue. Aliquam vel sem efficitur, condimentum enim vel, porta massa. Curabitur tempor turpis a gravida molestie. Aenean nisi sapien, egestas facilisis sagittis id, pretium sit amet orci. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed elit odio, porta ut tempor ut, suscipit at ante.'

paragraphs = [
    paragraph_1,
    paragraph_2,
    paragraph_3,
    paragraph_4,
    paragraph_5
]

count = 0
for paragraph in paragraphs:
    count += len(paragraph)
    # for word in paragraph.split(''):
    #     count += 1

print('Count: {} characters'.format(count))
