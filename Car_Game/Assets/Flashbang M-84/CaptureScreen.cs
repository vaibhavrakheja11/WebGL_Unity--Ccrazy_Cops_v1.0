using System.Collections;
using UnityEngine.UI;
using System.Collections.Generic;
using UnityEngine;


public class CaptureScreen : MonoBehaviour
{
    // Start is called before the first frame update

    public bool cap;
    public bool startFading;


    RawImage image;
    FadeOut fadeOut;


    void Start()
    {
        image = GameObject.FindGameObjectWithTag("OverallTexture").GetComponent<RawImage>();
        fadeOut = image.transform.GetComponent<FadeOut>();

    }

    // Update is called once per frame
    void Update()
    {
        if(startFading)
        {
            fadeOut.Fade = true;
            startFading = false;
        }
    }

    public static Texture Capture(Rect captureZone, int DesX, int desY)
    {
        Texture2D result;
        result = new Texture2D(Screen.width, Screen.height, TextureFormat.RGB24, false);
        Debug.Log("Vaibhav2");
        result.Apply();

        return result;

    }

    void OnPostRender()
    {
        if(cap)
        {
        image.texture = Capture(new Rect(0,0,Screen.width, Screen.height),0,0);
        cap = false;
        }
    }


}
