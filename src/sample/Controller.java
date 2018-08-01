package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

import java.awt.*;
import java.io.IOException;

public class Controller {
    @FXML
    private GridPane rooPane;
    private Stage stage;
    public void homePressed()
    {

    }

    public void playlistPressed()
    {

    }

    public void settingsPressed()
    {

    }

    public void aboutPressed(ActionEvent event) throws IOException {
        GridPane pane = FXMLLoader.load(getClass().getResource("about.fxml"));
        rooPane.getChildren().setAll(pane);
    }
}
