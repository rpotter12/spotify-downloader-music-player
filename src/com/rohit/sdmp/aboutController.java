package com.rohit.sdmp;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.GridPane;

import java.io.IOException;

public class aboutController {


    @FXML
    private GridPane aboutrootPane;
    //Stage stage;
    public void homePressed() throws IOException {
        GridPane homepane = FXMLLoader.load(getClass().getResource("home.fxml"));
        aboutrootPane.getChildren().setAll(homepane);
    }

    public void playlistPressed() throws IOException {
        GridPane playpane = FXMLLoader.load(getClass().getResource("playlist.fxml"));
        aboutrootPane.getChildren().setAll(playpane);
    }

    public void settingsPressed() throws IOException {
        GridPane settingpane = FXMLLoader.load(getClass().getResource("settings.fxml"));
        aboutrootPane.getChildren().setAll(settingpane);
    }

    public void aboutPressed() throws IOException {
        GridPane pane = FXMLLoader.load(getClass().getResource("about.fxml"));
        aboutrootPane.getChildren().setAll(pane);
    }



}


