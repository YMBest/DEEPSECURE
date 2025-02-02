import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import config

def get_data_loaders():
    print('==> Preparing Imagenet 10 class data..')
    # Data loading code
    traindir = config.imagenet10_traindir # Path to the training data
    valdir = config.imagenet10_valdir # Path to the validation data

    # Normalization transform: scales the image tensors
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225]) # Standard ImageNet normalization values
    
    # Define the data loader for the training dataset
    train_loader = torch.utils.data.DataLoader(
        datasets.ImageFolder(traindir, transforms.Compose([
            # Data augmentation: random resizing and cropping to 224x224
            transforms.RandomResizedCrop(224),
            # Data augmentation: random horizontal flip
            transforms.RandomHorizontalFlip(),
            # Convert images to PyTorch tensors
            transforms.ToTensor(),
            normalize,
        ])),
        batch_size=config.batch_size, shuffle=True,
        num_workers=4, pin_memory=True)
    
    # Define the data loader for the validation dataset
    val_loader = torch.utils.data.DataLoader(
        datasets.ImageFolder(valdir, transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            normalize,
        ])),
        batch_size=config.batch_size, shuffle=True,
        num_workers=4, pin_memory=True)

    return train_loader, val_loader
