from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc
from sklearn.linear_model import LogisticRegression

np.random.seed(42)
n_data = 5000

X1 = np.random.normal(loc=2.0, scale=1.0, size=n_data)
X2 = np.random.normal(loc=-1.0, scale=2.0, size=n_data)
X3 = np.random.rand(n_data)

# Introducimos missing en un % de X1 y X2
midx1 = np.random.choice(n_data, size=int(0.15*n_data), replace=False)
midx2 = np.random.choice(n_data, size=int(0.10*n_data), replace=False)
X1[midx1] = np.nan
X2[midx2] = np.nan

# Generamos y con una lógica logística
noise = np.random.normal(0, 0.5, size=n_data)
logits = 0.8*np.nan_to_num(X1, nan=2.0) - 1.2*np.nan_to_num(X2, nan=-1.0) + 2.0*X3 + noise
p = 1/(1 + np.exp(-logits))
y_data = np.random.binomial(1, p)

df_leakage = pd.DataFrame({
    'X1': X1,
    'X2': X2,
    'X3': X3,
    'target': y_data
})

train_df_leak, test_df_leak = train_test_split(df_leakage, test_size=0.3,
                                               random_state=42, stratify=df_leakage['target'])

X_train_leak = train_df_leak.drop('target', axis=1)
y_train_leak = train_df_leak['target']
X_test_leak = test_df_leak.drop('target', axis=1)
y_test_leak = test_df_leak['target']

# ---- PIPELINE INCORRECTO ----
X_all = pd.concat([X_train_leak, X_test_leak], axis=0).reset_index(drop=True)

imputer_inc = SimpleImputer(strategy='mean')
imputer_inc.fit(X_all)  # USANDO TODO (Train + Test)

X_train_inc = imputer_inc.transform(X_train_leak)
X_test_inc  = imputer_inc.transform(X_test_leak)

scaler_inc = StandardScaler()
scaler_inc.fit(imputer_inc.transform(X_all))  # USANDO TODO

X_train_inc_scl = scaler_inc.transform(X_train_inc)
X_test_inc_scl  = scaler_inc.transform(X_test_inc)

model_inc = LogisticRegression(max_iter=1000)
model_inc.fit(X_train_inc_scl, y_train_leak)

y_pred_inc_train = model_inc.predict(X_train_inc_scl)
y_pred_inc_test  = model_inc.predict(X_test_inc_scl)

acc_inc_train = accuracy_score(y_train_leak, y_pred_inc_train)
acc_inc_test  = accuracy_score(y_test_leak, y_pred_inc_test)

print("\n==== DATA LEAKAGE: PIPELINE INCORRECTO ====")
print(f"Train Accuracy: {acc_inc_train:.4f}")
print(f"Test Accuracy : {acc_inc_test:.4f}")

# ---- PIPELINE CORRECTO ----
imputer_cor = SimpleImputer(strategy='mean')
imputer_cor.fit(X_train_leak)  # Solo con train

X_train_cor = imputer_cor.transform(X_train_leak)
X_test_cor  = imputer_cor.transform(X_test_leak)

scaler_cor = StandardScaler()
scaler_cor.fit(X_train_cor)  # Solo con train

X_train_cor_scl = scaler_cor.transform(X_train_cor)
X_test_cor_scl  = scaler_cor.transform(X_test_cor)

model_cor = LogisticRegression(max_iter=1000)
model_cor.fit(X_train_cor_scl, y_train_leak)

y_pred_cor_train = model_cor.predict(X_train_cor_scl)
y_pred_cor_test  = model_cor.predict(X_test_cor_scl)

acc_cor_train = accuracy_score(y_train_leak, y_pred_cor_train)
acc_cor_test  = accuracy_score(y_test_leak, y_pred_cor_test)

print("\n==== DATA LEAKAGE: PIPELINE CORRECTO ====")
print(f"Train Accuracy: {acc_cor_train:.4f}")
print(f"Test Accuracy : {acc_cor_test:.4f}")

# Visualización comparativa
approaches = ['Incorrecto', 'Correcto']
train_accs = [acc_inc_train, acc_cor_train]
test_accs  = [acc_inc_test,  acc_cor_test]

plt.figure(figsize=(6,4))
x_ = np.arange(len(approaches))
width = 0.3

bars_train = plt.bar(x_ - width/2, train_accs, width, label='Train Accuracy')
bars_test  = plt.bar(x_ + width/2, test_accs,  width, label='Test Accuracy')

plt.xticks(x_, approaches)
plt.ylim([0,1])
plt.title("Comparación de Accuracies (Data Leakage)")
plt.legend()

for bar in bars_train+bars_test:
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, h+0.01,
             f"{h:.3f}", ha='center')

plt.tight_layout()
plt.show()

print("""
Conclusión:
Cuando usamos todo el dataset (incluyendo test) para imputar/escalar, 
tenemos Data Leakage, produciendo resultados "inflados". 
La forma correcta es ajustar los transformadores (Imputer/Scaler) 
SOLO con datos de entrenamiento y luego aplicarlos a test.
""")

# FIN DEL SCRIPT