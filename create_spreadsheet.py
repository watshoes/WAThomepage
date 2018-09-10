class Spreadsheet(object):
    def add_values(self,values):
        with open("beta_testers.txt",'a') as data:
            entry = values['name1'], values['email1'],values['gender'],values['FavoriteShoe']
            data.write("\nentry: {}".format( entry))
