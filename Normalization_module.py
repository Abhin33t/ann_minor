__author__ = 'Abhineet Saxena'

"""
Indian Liver Patient Database: Dataset Normalization Program
"""
def minMax(listvar_recs, list_indices):
    #print 'Entered minMax'
    len_list = len(list_indices)
    max_list = [-999999999.0]*len_list
    min_list = [999999999.0]*len_list
    for iter_rec in listvar_recs:
        for jterv in xrange(len_list):
            if iter_rec[list_indices[jterv]] > max_list[jterv]:
                max_list[jterv] = iter_rec[list_indices[jterv]]
            if iter_rec[list_indices[jterv]] < min_list[jterv]:
                min_list[jterv] = iter_rec[list_indices[jterv]]
    #print max_list, min_list
    return (max_list, min_list)

def Normalize(elem, min, max):
    return ((elem - min)/(max - min))

def normalizeAttrib(listvar_recs, list_indices):
    """
    The function will be utilized to normalize the input that has been obtained. Normalization occurs
    in accordance to the formula specified by the method 'Normalize'.
    :param
    listvar_recs: The list of records containing the attributes to be Normalized.
    list_indices: The list of indices denoting the specific attributes that must be normalized.
    :return:
    listvar_recs: The list of records whose values have been normalized.
    """
    len_list = len(list_indices)
    max_list, min_list = minMax(listvar_recs, list_indices)
    for recvar in listvar_recs:  # Takes each record at a time
        # iterv: The index that runs through and synchronizes the access to list_indices and max and min lists
        for iterv in xrange(len_list):
                # Normalizes the attributes with indices referenced by iterv from list_indices.
                recvar[list_indices[iterv]] = Normalize(recvar[list_indices[iterv]], min_list[iterv], max_list[iterv])
    return listvar_recs

if __name__ == '__main__':
    newFile = open('ilpd_data.csv', 'r')
    outFile = open('ilpd_normalized_data.csv', 'w')
    records_list = []
    count = 0
    for line in newFile:
        newline = line.strip().split(",")
        if newline[1] == 'Male':
            newline[1] = 0
        else:
            newline[1] = 1
        #print newline
        count += 1
        try:
            newline = [float(elem) for elem in newline]
            if newline[10] == 2.0:
                newline[10] = 0.0
            records_list.append(newline)
        except ValueError:
            print 'Skipped row with number: {0} and string as: {1}'.format(count, newline)
    records_list = normalizeAttrib(records_list, [0, 2, 3, 4, 5, 6, 7, 8, 9])
    for iterv in records_list:
        #print iterv
        write_str = ','.join([str(elem) for elem in iterv]) + '\n'
        print write_str
        outFile.write(write_str)