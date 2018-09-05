package com.rohit.sdmp;

import javafx.application.HostServices;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.scene.media.*;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;
import javafx.stage.Window;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;

import static javafx.application.Application.launch;

public class playlistController {


    @FXML
    private GridPane playlistrootPane;
    final FileChooser fileChooser = new FileChooser();
    Stage primaryStage;
    private String resource;
    Process p=Runtime.getRuntime().exec("/usr/share/applications/Rhythmbox");

    public playlistController() throws IOException {
    }

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
        String files= "%file";
        if(file !=null)
        {
            //openFile(file.toURI().toString());
            file;
            InputStream inputStream = p.getInputStream();
        }
    }


    // media player
    /*private void openFile(String file) {

            primaryStage.setTitle("Media Player");
            Group root = new Group();
            Scene scene = new Scene(root, 540, 241);

            // create media player
            Media media = new Media (file);
            MediaPlayer mediaPlayer = new MediaPlayer(media);
            mediaPlayer.setAutoPlay(true);

            MediaControl mediaControl = new MediaControl(mediaPlayer);
            scene.setRoot(mediaControl);

            primaryStage.setScene(scene);
            primaryStage.sizeToScene();
            primaryStage.show();


    }*/
}


