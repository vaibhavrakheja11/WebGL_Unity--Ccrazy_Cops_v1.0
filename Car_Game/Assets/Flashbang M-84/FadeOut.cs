using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class FadeOut : MonoBehaviour
{
    // Start is called before the first frame update

    public bool Fade;

    RawImage image;
    RawImage colorMultiplier;

    float timer;
    Color color;
    Color color2;
    bool count;

    void Start()
    {
        image = GetComponent<RawImage>();
        RawImage[] imgs = transform.parent.GetComponentsInChildren<RawImage>();
        foreach(RawImage im in imgs)
        {
            if(im != image)
            {
                colorMultiplier = im;
            }
        }
        color = image.color;
        color.a = 0;
        image .color = color;

        color2 = colorMultiplier.color;
        colorMultiplier.color = color2;
    }

    // Update is called once per frame
    void Update()
    {
        if(Fade)
        {
            color.a = 1f;
            image.color = color;

            color2.a = 0.7f;
            colorMultiplier.color = color2;

            image.enabled = true;
            colorMultiplier.enabled = true;
            count = true;
            Fade = false;
        }

        if(count)
        {
            timer += Time.deltaTime;
            if(timer>5)
            {
                color.a -= Time.deltaTime * 0.1f;
                image.color = color;
                color2.a -= Time.deltaTime * 0.05f;
                colorMultiplier.color = color2;


                if(image.color.a <= 0)
                {
                    timer = 0;
                    count =  false;
                }
            }
            else
            {
                image.enabled = false;
                colorMultiplier.enabled = false;
            }
        }
    }

}
