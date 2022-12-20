def unionCYK(cek, cekLen):
    if cekLen == 1: return cek[cekLen-1]
    else: return list(set(cek[cekLen-1]).union(set(unionCYK(cek, cekLen-1))))

def hitungCellTabel(produksi, tabel, i, j): 
    '''
        Pada table filling terdapat rumus menentukan tiap cell yang akan dihitung yaitu:
        (X[i,i], X[i+1,j]) U (X[i,i+1], X[i+2,j]) U ... (X[i,j-1], X[j,j])
        
        Misalkan nilai i dan j yang akan di-pass adalah:
        i = 1
        j = 4
        Maka perhitungannya akan seperti:
        (X[1,1], X[2,4]) U (X[1,2], X[3,4]) U (X[1,3], X[4,4])
        Jika diperhatikan, nilai j akan tetap namun nilai dari i akan mengalami incremental
        sebanyak k (dengan nilai k awal = 0) untuk cell pertama (X[1,1]) dan k+1 untuk cell
        kedua (X[2,4]). Dengan cara ini, semua perhitungan letak cell akan memenuhi rumus
        untuk perulangan dari i ke j.

    '''
    
    k = 0
    hasil = []
    cek = []
    
    while(i+k+1 <= j):
        temp = []
        for a in range(len(tabel[i][i+k])):
            for b in range(len(tabel[i+k+1][j])):
                temp.append(tabel[i][i+k][a] + ' ' + tabel[i+k+1][j][b])

        cek.append(temp)
        k += 1

    cek = unionCYK(cek, len(cek))

    for key, val in produksi.items():
        for c in cek:
            if c in val:
                hasil.append(key)
                break
    
    hasil = list(dict.fromkeys(hasil))
    return hasil

def hitungCYK(produksi, str, start):
    '''
        Bentuk triangular table dalam program ini:
        [X[1,1]] [X[1,2]] [X[1,3]]
        [      ] [X[2,2]] [X[2,3]]
        [      ] [      ] [X[3,3]]
        dst...

        Diagonal utama tabel di atas akan menjadi "baris pertama"
        Lalu "baris kedua" dilanjutkan di diagonal bagian kanan "baris pertama"
        Dan seterusnya untuk baris-baris selanjutnya
        
    '''

    strLen = len(str)
    tabel = []
    i = 0
    for s in str:
        baris = []
        cell = []
        for j in range(i): baris.append([])
        for key, val in produksi.items():
            if s in val: cell.append(key)
        baris.append(cell)
        tabel.append(baris)
        i += 1

    for i in range(strLen-1):
        for j in range(strLen-i-1):
            
            k = i+j+1
            hasil = hitungCellTabel(produksi, tabel, j, k)
            tabel[j].append(hasil)

    if start in tabel[0][strLen-1]: return True
    else: return False