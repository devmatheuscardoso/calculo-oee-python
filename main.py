# ============================================================
# SISTEMA DE CÁLCULO DE OEE (Eficiência Global do Equipamento)
# ============================================================

print("="*50)
print(" 📊 TERMINAL DE GESTÃO DE PRODUÇÃO - TURNO A")
print("="*50)

# 1. ENTRADA DE DADOS
tempo_planejado = int(input("Tempo total planejado para o turno (minutos): "))
tempo_paradas = int(input("Tempo total de máquina parada por falha (minutos): "))
meta_producao = int(input("Meta de peças para este turno: "))
pecas_produzidas = int(input("Total de peças produzidas (boas + ruins): "))
pecas_refugos = int(input("Quantidade de peças rejeitadas (refugo): "))
print("\n ⚙️ Processando dados do Turno... Aguarde... \n")

# 2. PROCESSAMENTO 

# Cálculo 1: Disponibilidade
tempo_operando = tempo_planejado - tempo_paradas
taxa_disponibilidade = (tempo_operando / tempo_planejado) * 100

# Cálculo 2: Performance
taxa_performance = (pecas_produzidas / meta_producao) * 100

# Cálculo 3: Qualidade
pecas_boas = pecas_produzidas - pecas_refugos
taxa_qualidade = (pecas_boas / pecas_produzidas) * 100

# Cálculo 4: OEE Global
oee_final = (taxa_disponibilidade / 100) * (taxa_performance / 100) * (taxa_qualidade / 100) * 100

# 3. SAÍDA DE DADOS
print("="*50)
print("📈 RELATÓRIO DE DESEMPENHO (OEE)")
print("="*50)
print(f"✅ Peças Aprovadas: {pecas_boas} de {pecas_produzidas}")
print(f"⏱️ Disponibilidade da Máquina: {taxa_disponibilidade:.1f}%")
print(f"🚀 Performance de Production: {taxa_performance:.1f}%")
print(f"🛡️ Índice de Qualidade: {taxa_qualidade:.1f}%")
print("-" *50)
print(f"🏆 OEE FINAL DO TURNO: {oee_final:.1f}%")
print("="*50)
