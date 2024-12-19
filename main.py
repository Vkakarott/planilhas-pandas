import pandas as pd

def separar_turmas_por_email(base_entrada, turmaA_entrada, turmaB_entrada, turmaC_entrada):
    # Carregando as bases de dados
    df_base = pd.read_csv(base_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    
    print("Colunas da Base: ", df_base.columns)

    df_turmaA = pd.read_csv(turmaA_entrada, encoding='utf-8-sig', sep=',') 
    df_turmaB = pd.read_csv(turmaB_entrada, encoding='utf-8-sig', sep=',') 
    df_turmaC = pd.read_csv(turmaC_entrada, encoding='utf-8-sig', sep=',') 

    print("Colunas da Turma A: ", df_turmaA.columns)
    print("Colunas da Turma B: ", df_turmaB.columns)
    print("Colunas da Turma C: ", df_turmaC.columns)

    # Limpando os nomes das colunas
    df_turmaA.columns = df_turmaA.columns.str.strip().str.replace('ï»¿', '').str.replace('“', '').str.replace('”', '')
    df_turmaB.columns = df_turmaB.columns.str.strip().str.replace('ï»¿', '').str.replace('“', '').str.replace('”', '')
    df_turmaC.columns = df_turmaC.columns.str.strip().str.replace('ï»¿', '').str.replace('“', '').str.replace('”', '')
    
    # Filtrando as turmas
    df_turmaA_emails = df_turmaA['Endereço de email'].tolist()
    df_turmaB_emails = df_turmaB['Endereço de email'].tolist()
    df_turmaC_emails = df_turmaC['Endereço de email'].tolist()

    df_turmaA_final = df_base[df_base['Endereço de email'].isin(df_turmaA_emails)]
    df_turmaB_final = df_base[df_base['Endereço de email'].isin(df_turmaB_emails)]
    df_turmaC_final = df_base[df_base['Endereço de email'].isin(df_turmaC_emails)]

    # Removendo colunas indesejadas
    cols_to_drop = ['Identificação de usuário', 'Unnamed: 1', 'Endereço de email']
    df_turmaA_final = df_turmaA_final.drop(columns=cols_to_drop)
    df_turmaB_final = df_turmaB_final.drop(columns=cols_to_drop)
    df_turmaC_final = df_turmaC_final.drop(columns=cols_to_drop)

    # Concatenando as colunas 'Nome' e 'Sobrenome' e criando a nova coluna
    df_turmaA_final['Nome Completo'] = df_turmaA_final['Nome'] + ' ' + df_turmaA_final['Sobrenome']
    df_turmaB_final['Nome Completo'] = df_turmaB_final['Nome'] + ' ' + df_turmaB_final['Sobrenome']
    df_turmaC_final['Nome Completo'] = df_turmaC_final['Nome'] + ' ' + df_turmaC_final['Sobrenome']

    # Removendo as colunas 'Nome' e 'Sobrenome'
    df_turmaA_final = df_turmaA_final.drop(columns=['Nome', 'Sobrenome'])
    df_turmaB_final = df_turmaB_final.drop(columns=['Nome', 'Sobrenome'])
    df_turmaC_final = df_turmaC_final.drop(columns=['Nome', 'Sobrenome'])

    # Reorganizando a coluna 'Nome Completo' para ser a primeira
    cols = ['Nome Completo'] + [col for col in df_turmaA_final.columns if col != 'Nome Completo']
    df_turmaA_final = df_turmaA_final[cols]
    df_turmaB_final = df_turmaB_final[cols]
    df_turmaC_final = df_turmaC_final[cols]

    # Salvando os resultados
    df_turmaA_final.to_csv("turmaA_filtrada.csv", index=False, sep=';', encoding='latin1')
    df_turmaB_final.to_csv("turmaB_filtrada.csv", index=False, sep=';', encoding='latin1')
    df_turmaC_final.to_csv("turmaC_filtrada.csv", index=False, sep=';', encoding='latin1')

# Defina os caminhos dos arquivos de entrada
arquivo_base = "Base.csv"
arquivo_turmaA = "turmaA.csv"
arquivo_turmaB = "turmaB.csv"
arquivo_turmaC = "turmaC.csv"

# Chamando a função para separar as turmas
separar_turmas_por_email(arquivo_base, arquivo_turmaA, arquivo_turmaB, arquivo_turmaC)
