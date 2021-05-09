package main

import (
	"fmt"

	"github.com/dmitryikh/leaves"
	"github.com/dmitryikh/leaves/mat"
	"github.com/dmitryikh/leaves/util"
)

func main() {
	// loading test data
	test, err := mat.DenseMatFromCsvFile("iris_test.tsv", 0, false, "\t", 0.0)
	if err != nil {
		panic(err)
	}

	// loading model
	model, err := leaves.LGEnsembleFromFile("lg_iris.model", true)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Name: %s\n", model.Name())
	fmt.Printf("NFeatures: %d\n", model.NFeatures())
	fmt.Printf("NOutputGroups: %d\n", model.NOutputGroups())
	fmt.Printf("NEstimators: %d\n", model.NEstimators())
	fmt.Printf("Transformation: %s\n", model.Transformation().Name())

	// loading true predictions as DenseMat
	truePredictions, err := mat.DenseMatFromCsvFile("lg_iris_true_predictions.txt", 0, false, "\t", 0.0)
	if err != nil {
		panic(err)
	}
	truePredictionsRaw, err := mat.DenseMatFromCsvFile("lg_iris_true_predictions_raw.txt", 0, false, "\t", 0.0)
	if err != nil {
		panic(err)
	}

	// preallocate slice to store model predictions
	predictions := make([]float64, test.Rows*model.NOutputGroups())
	// do predictions
	model.PredictDense(test.Values, test.Rows, test.Cols, predictions, 0, 1)
	// compare results
	const tolerance = 1e-6
	if err := util.AlmostEqualFloat64Slices(truePredictions.Values, predictions, tolerance); err != nil {
		panic(fmt.Errorf("different predictions: %s", err.Error()))
	}

	// compare raw predictions (before transformation function)
	rawModel := model.EnsembleWithRawPredictions()
	rawModel.PredictDense(test.Values, test.Rows, test.Cols, predictions, 0, 1)
	if err := util.AlmostEqualFloat64Slices(truePredictionsRaw.Values, predictions, tolerance); err != nil {
		panic(fmt.Errorf("different raw predictions: %s", err.Error()))
	}
	fmt.Println("Predictions the same!")
}
