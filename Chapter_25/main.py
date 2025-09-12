URI = ""

from pymongo import MongoClient

client = MongoClient(URI)

# print(client.admin.command('ping'))

db = client['students']
coll = db['cdshpyt']


# Create__________
# coll.insert_one({
#     'name':'Rakesh',
#     'roll':6737843267,
#     'phone':6296386131,
# })

# print(coll.insert_one({
#     'name':'Rimi',
#     'roll':6737848537,
#     'phone':8926731111,
# }))

# Read_______
# all_data = coll.find()
# [print(data) for data in all_data]

# all_data = coll.find_one({'name':'Rakesh'})
# print(all_data)

# Update__________
# coll.update_one({'name':'Rakesh'},{'$set':{'name':'Rakesh Kundu'}})
# coll.update_one({'name':'Rimi'},{'$set':{'name':'Rimi Bairi'}})

# Delete_____________
# coll.delete_one({'name':'Rakesh Kundu'})
# coll.delete_one({'name':'Rimi Bairi'})


