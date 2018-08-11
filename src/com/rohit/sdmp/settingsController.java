package com.rohit.sdmp;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.GridPane;

import java.io.IOException;

public class settingsController {


    @FXML
    private GridPane settingsrootPane;
    //Stage stage;
    public void homePressed() throws IOException {
        GridPane homepane = FXMLLoader.load(getClass().getResource("home.fxml"));
        settingsrootPane.getChildren().setAll(homepane);
    }

    public void playlistPressed() throws IOException {
        GridPane playpane = FXMLLoader.load(getClass().getResource("playlist.fxml"));
        settingsrootPane.getChildren().setAll(playpane);
    }

    public void settingsPressed() throws IOException {
        GridPane settingpane = FXMLLoader.load(getClass().getResource("settings.fxml"));
        settingsrootPane.getChildren().setAll(settingpane);
    }

    public void aboutPressed() throws IOException {
        GridPane pane = FXMLLoader.load(getClass().getResource("about.fxml"));
        settingsrootPane.getChildren().setAll(pane);
    }



}
