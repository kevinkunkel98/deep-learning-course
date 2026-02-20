"""
PyTorch Exam Prep – Binder Deep Learning Klausur
Covers: Tensors, Broadcasting, Linear Algebra, Squeeze/Unsqueeze,
        Full Training Loop (DataSet, DataLoader, Train, Eval)
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np

print("=" * 60)
print("1. TENSOR BASICS")
print("=" * 60)

# Creation
a = torch.rand((3,))          # 1-tensor (vector)
b = torch.rand((2, 4))        # 2-tensor (matrix)
c = torch.rand((7, 5, 3))     # 3-tensor

print(f"Shape: {c.shape}, Dtype: {c.dtype}, Device: {c.device}")

# Fixed-value tensors
x = torch.zeros((5, 1))
y = torch.ones((5,))
z = torch.full((2, 3), 3.14)
r = torch.randn((2, 3))       # normal distributed

# dtype conversion
e = c.to(torch.float64)       # DOUBLE = slow on GPU!
# device: c.to('cuda:0') if GPU available

# Reshape with view (-1 = joker/wildcard)
x = torch.ones((10,))
y = x.view((2, 5))
z = x.view((-1, 5))           # -1 inferred as 2
print(f"view(-1,5): {z.shape}")

# CAREFUL with view ordering!
x = torch.ones((4, 2, 3))
y = x.view((-1, 12))          # shape (2, 12) – elements filled row-major
print(f"(4,2,3) -> view(-1,12): {y.shape}")

print("\n" + "=" * 60)
print("2. NUMPY INTERFACING")
print("=" * 60)

# To numpy (MUST be on CPU, no grad)
np_c = c.data.cpu().numpy()
print(f"Tensor -> numpy: {type(np_c)}")

# From numpy
arr = np.ones((3, 5), dtype='float32')
t1 = torch.tensor(arr)          # COPIES data
t2 = torch.as_tensor(arr)       # NO copy (shares memory!)
t3 = torch.from_numpy(arr)      # NO copy (shares memory!)
# Danger: shared memory = side effects!

print("\n" + "=" * 60)
print("3. BROADCASTING – Klausurrelevant!")
print("=" * 60)

# Rules:
# 1) Smaller tensor padded with 1s on LEFT until same ndim
# 2) Check compatibility: dims must be equal OR one of them is 1
#    (if both >1 and unequal -> ERROR)
# 3) Dim with size 1 gets replicated to match the other

# Examples from slides:
a = torch.ones((4,))
b = torch.ones((1, 4))
print(f"(4) + (1,4) -> {(a + b).shape}")        # (1, 4)

a = torch.ones((4,))
b = torch.ones((4, 1))
print(f"(4) + (4,1) -> {(a + b).shape}")        # (4, 4) !!!

a = torch.ones((3,))
b = torch.ones((4, 1))
print(f"(3) + (4,1) -> {(a + b).shape}")        # (4, 3)

# a = torch.ones((3,)); b = torch.ones((1,4))
# a + b -> ERROR! (3) -> (1,3), then 3 vs 4 = incompatible

# Detailed walkthrough:
# start       -> after left-pad -> after copy
# (2,3)          (1,2,3)           (5,2,3)
# (5,1,3)        (5,1,3)           (5,2,3)

# (1,7)          (1,1,1,7)         (5,2,3,7)
# (5,2,3,7)      (5,2,3,7)         (5,2,3,7)

# (4,1)          (1,4,1)           ERR (4 vs 3, 1 vs 7)
# (2,3,7)        (2,3,7)           ERR

print("\n" + "=" * 60)
print("4. LINEAR ALGEBRA")
print("=" * 60)

# dot product: vector · vector -> scalar
v1 = torch.tensor([1., 2., 3.])
v2 = torch.tensor([4., 5., 6.])
print(f"dot: {torch.dot(v1, v2)}")  # 1*4 + 2*5 + 3*6 = 32

# mm: matrix multiplication (2-tensor x 2-tensor only!)
A = torch.randn((3, 4))
B = torch.randn((4, 5))
C = torch.mm(A, B)
print(f"mm: ({A.shape}) x ({B.shape}) -> {C.shape}")  # (3, 5)

# bmm: batched matrix multiplication (3-tensor x 3-tensor)
# batch dim must match, inner dims must be compatible
A = torch.randn((8, 3, 4))
B = torch.randn((8, 4, 5))
C = torch.bmm(A, B)
print(f"bmm: ({A.shape}) x ({B.shape}) -> {C.shape}")  # (8, 3, 5)
# = for each b: mm(A[b,:,:], B[b,:,:])

print("\n" + "=" * 60)
print("5. SQUEEZE / UNSQUEEZE")
print("=" * 60)

# unsqueeze: insert singleton dim
v = torch.randn((5,))
print(f"Original: {v.shape}")
print(f"unsqueeze(0): {v.unsqueeze(0).shape}")  # (1, 5)
print(f"unsqueeze(1): {v.unsqueeze(1).shape}")  # (5, 1)

# squeeze: remove singleton dim
t = torch.randn((3, 1, 5))
print(f"squeeze(1): {t.squeeze(1).shape}")       # (3, 5)

# Practical use: vector-matrix product via mm
v = torch.randn((4,))        # 1-tensor, can't use mm directly
A = torch.randn((4, 3))
result = torch.mm(v.unsqueeze(0), A).squeeze(0)  # (1,4)·(4,3)->(1,3)->(3,)
print(f"v @ A via mm: {result.shape}")

# transpose and permute for shape fixing
t = torch.randn((2, 3, 4))
print(f"transpose(1,2): {t.transpose(1, 2).shape}")  # (2, 4, 3)
print(f"permute(2,0,1): {t.permute(2, 0, 1).shape}") # (4, 2, 3)

print("\n" + "=" * 60)
print("6. FULL TRAINING LOOP – FashionMNIST Logistic Regression")
print("=" * 60)

# ============================================================
# 6a. Data Transforms & Dataset
# ============================================================
from torchvision import datasets, transforms

torch.manual_seed(3)  # Reproducibility!

datatransforms = transforms.Compose([
    transforms.ToTensor(),
    # Normalize: (pixel - mean) / std, per channel
    # Makes training more stable, gradients centered around 0
    transforms.Normalize((0.1307,), (0.3081,))
])

ds_trainval = datasets.FashionMNIST('./data', train=True, download=True,
                                     transform=datatransforms)
ds_test = datasets.FashionMNIST('./data', train=False, download=True,
                                 transform=datatransforms)

# Train/Val split
num_train = int(0.8 * len(ds_trainval))
num_val = len(ds_trainval) - num_train
indices = torch.randperm(len(ds_trainval)).tolist()
train_idx, val_idx = indices[:num_train], indices[num_train:]

from torch.utils.data import SubsetRandomSampler

batchsize = 32
dl_train = torch.utils.data.DataLoader(ds_trainval, batch_size=batchsize,
                                        sampler=SubsetRandomSampler(train_idx))
dl_val = torch.utils.data.DataLoader(ds_trainval, batch_size=batchsize,
                                      sampler=SubsetRandomSampler(val_idx))
dl_test = torch.utils.data.DataLoader(ds_test, batch_size=batchsize, shuffle=False)

print(f"Train: {num_train}, Val: {num_val}, Test: {len(ds_test)}")

# ============================================================
# 6b. Model Definition
# ============================================================
class OneLinear(nn.Module):
    """Logistic regression = 1-layer NN, no hidden layers"""
    def __init__(self, in_dims, num_classes):
        super().__init__()
        # Parameters wrapped in nn.Parameter -> trainable!
        self.w = nn.Parameter(torch.randn((in_dims, num_classes)), requires_grad=True)
        self.bias = nn.Parameter(torch.zeros(num_classes), requires_grad=True)

    def forward(self, x):
        v = x.view((-1, 28 * 28))        # flatten: (batch, 1, 28, 28) -> (batch, 784)
        y = self.bias + torch.mm(v, self.w)  # linear: (batch, 784) @ (784, 10) -> (batch, 10)
        return y  # raw logits, CrossEntropyLoss applies softmax internally

device = torch.device("cpu")
model = OneLinear(28 * 28, 10).to(device)

# ============================================================
# 6c. Loss & Optimizer
# ============================================================
criterion = nn.CrossEntropyLoss()
# CrossEntropyLoss = softmax + neg-log-likelihood combined

# ============================================================
# 6d. Training Function
# ============================================================
def train_epoch(model, trainloader, criterion, device, optimizer):
    model.train()  # !!! WICHTIG: train mode (BatchNorm/Dropout aktiv)
    losses = []
    for batch_idx, (inputs, labels) in enumerate(trainloader):
        inputs = inputs.to(device)
        labels = labels.to(device)

        outputs = model(inputs)           # forward pass
        loss = criterion(outputs, labels)  # compute loss

        optimizer.zero_grad()              # reset gradients!
        loss.backward()                    # compute gradients
        optimizer.step()                   # update parameters

        losses.append(loss.item())
    return losses

# ============================================================
# 6e. Evaluation Function
# ============================================================
def evaluate(model, dataloader, device):
    model.eval()  # !!! WICHTIG: eval mode (BatchNorm/Dropout deaktiviert)
    with torch.no_grad():  # !!! Keine Gradienten berechnen
        correct = 0
        total = 0
        for inputs, labels in dataloader:
            inputs = inputs.to(device)
            outputs = model(inputs).cpu()

            _, preds = torch.max(outputs, 1)  # argmax -> predicted class
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    return correct / total

# ============================================================
# 6f. Hyperparameter Search + Training Loop
# ============================================================
maxnumepochs = 3
lrates = [0.01, 0.001]

best_hyperparameter = None
weights_chosen = None
bestmeasure = 0

for lr in lrates:
    print(f"\n--- Training with lr={lr} ---")
    # Re-init model for each hyperparameter
    model = OneLinear(28 * 28, 10).to(device)
    optimizer = optim.SGD(model.parameters(), lr=lr, momentum=0.9)

    best_epoch_measure = 0
    best_weights = None

    for epoch in range(maxnumepochs):
        losses = train_epoch(model, dl_train, criterion, device, optimizer)

        val_acc = evaluate(model, dl_val, device)
        print(f"  Epoch {epoch}: loss={np.mean(losses):.4f}, val_acc={val_acc:.4f}")

        if val_acc > best_epoch_measure:
            best_epoch_measure = val_acc
            best_weights = model.state_dict()  # save best weights

    # Compare across hyperparameters
    if best_epoch_measure > bestmeasure:
        bestmeasure = best_epoch_measure
        best_hyperparameter = lr
        weights_chosen = best_weights

# Final evaluation on TEST data (only once, after all HP search!)
model.load_state_dict(weights_chosen)
test_acc = evaluate(model, dl_test, device)
print(f"\n{'=' * 60}")
print(f"Best lr={best_hyperparameter}, Val acc={bestmeasure:.4f}, TEST acc={test_acc:.4f}")
print(f"{'=' * 60}")

print("\n" + "=" * 60)
print("ZUSAMMENFASSUNG – Klausur-Checkliste")
print("=" * 60)
print("""
✓ Tensor: shape, dtype, device
✓ Broadcasting: left-pad mit 1en, dann dim=1 wird kopiert
✓ mm (2D×2D), bmm (3D×3D), dot (1D·1D)
✓ unsqueeze(dim) = dim einfügen, squeeze(dim) = dim entfernen
✓ view(-1, n) zum Reshapen, -1 = Joker
✓ DataSet: __init__, __len__, __getitem__
✓ DataLoader: batch_size, shuffle/sampler
✓ model.train() beim Training, model.eval() beim Testen!
✓ torch.no_grad() beim Evaluieren!
✓ Training loop: forward -> loss -> zero_grad -> backward -> step
✓ Normalize: (pixel - mean) / std für stabileres Training
✓ CrossEntropyLoss = Softmax + NegLogLikelihood
✓ Hyperparameter-Suche auf VAL, finale Eval auf TEST (nur 1x!)
✓ torch.manual_seed() für Reproduzierbarkeit
""")
