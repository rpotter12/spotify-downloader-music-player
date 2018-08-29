package com.rohit.sdmp;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.GridPane;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.stage.Window;

import java.io.File;
import java.io.IOException;

public class playlistController {


    @FXML
    private GridPane playlistrootPane;
    final FileChooser fileChooser = new FileChooser();
    Stage primaryStage;
    //Stage stage;
    public void homePressed() throws IOException {
        GridPane homepane = FXMLLoader.load(getClass().getResource("home.fxml"));
        playlistrootPane.getChildren().setAll(homepane);
    }

    public void playlistPressed() throws IOException {
        GridPane playpane = FXMLLoader.load(getClass().getResource("playlist.fxml"));
        playlistrootPane.getChildren().setAll(playpane);
    }

    public void settingsPressed() throws IOException {
        GridPane settingpane = FXMLLoader.load(getClass().getResource("settings.fxml"));
        playlistrootPane.getChildren().setAll(settingpane);
    }

    public void aboutPressed() throws IOException {
        GridPane pane = FXMLLoader.load(getClass().getResource("about.fxml"));
        playlistrootPane.getChildren().setAll(pane);
    }


    public void choosePressed(ActionEvent actionEvent) {
        fileChooser.setTitle("select song");
        final File file = fileChooser.showOpenDialog(primaryStage);
    }
}
