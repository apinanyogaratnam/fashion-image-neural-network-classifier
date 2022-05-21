def evaluate(model, test_images, test_labels, should_evaluate=True):
    if should_evaluate:
        test_loss, test_acc = model.evaluate(test_images, test_labels)
        print("tested accuracy", test_acc)
